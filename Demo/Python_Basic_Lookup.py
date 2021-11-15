#Remember the gls_python module needs to be installed, see the gls python guide for instructions.

import gls_python.abgis as gis          # import the gls_python.abgis module and give it the alias gis. This means we can just use gis later
import gls_python.general as general    # import the gls_python.general module and give it the alias general. This means we can just use general later
import gls_python.adb as adb            # import the gls_python.adb module and give it the alias asb. This means we can just use adb later

# Note: The text within three """ are descriptions of the function. 
# When using an IDE, like VS Code, this text will be shown when hovering over a function when where it is being called from
 

def GetTableByName(iPartOfGISLayerName: str) -> adb.AlbionDataBase:
    """    
    To get a table we need to search for it amongst the gis layers
    This function takes a string (iPartOfGISLayerName) as input.
    This string can be an entire gis layer name of just any part of the name you wish to find.
    Be aware that if there are duplicate names then only the first found will be returned.
    ie if more than one model is loaded Wa_pipe could return any of the open models' pipe layers.
    """
    layers = gis.AlbionGisLayer() # Get the AlbionGisLayer object linking to Albion

    for i in range(layers.GetLayerCount()): # Loop through all the open loaded layers
        layer = layers.GetLayerByIndex(i) # Get the layer at the current index
        layername = layers.GetLayerName(layer) # Get the name of the current layer
        if iPartOfGISLayerName in layername: # Compare the layer name with the one given. If a portion is within the layer name the layer's table is returned
            return layers.GetTableFromLayerIndex(layer)	# Get the underlying table from the gis layer and return it for further use		
    
    general.ShowNotification(iPartOfGISLayerName + " not found", general.AlbionMessageTypes.ntError) # This will only be called if no matchin layer is found
    return None # return an empty result, this allows other functions to check if a table was found


def CheckFieldExists(iTable, iName: str) -> int:
    """
    Finding and checking fields can be repetitive, this functions tests a field exists and outputs an error
    -1 Will be returned if the field does not exist in the table
    """
    fieldindex = iTable.FieldIndex(iName) # Get the field index of the field within iTable
    if fieldindex == -1: # Test if the result was -1
        general.ShowNotification(iName + " not found in " + iTable.Name(), general.AlbionMessageTypes.ntError) # output an error message if the field was not found
    return fieldindex # Return then field index


def VLookup(fromTableName: str, fromKey: str, fromField: str, toTableName: str, toKey: str, toField: str):
    """
    This function is similar to an excel vlookup function
    fromTableName -> The table name that data needs to be copied from
    fromKey       -> The key field of the from table, the value in this field will be used to match with a to key
    fromField     -> The name of the field that data needs be copied from
    toTableName   -> The table name that data will be copied to
    toKey         -> The key field of the to table, the value in this field will be used to match with a from key	
    toField       -> The name of the field that data will be copied to
    """

    fr_tab = GetTableByName(fromTableName) # Find the from table if it exists 
    if fr_tab == None: # Test if a table was found
        return False # If not then stop the function and return false to indicate the function failed
		
    fld_fr_key = CheckFieldExists(fr_tab, fromKey) # Find the key field index
    fld_fr_value = CheckFieldExists(fr_tab, fromField) # find the to field index

    if fld_fr_value == -1 or fld_fr_key == -1: # test that both field exists
        return False # If one of the fields are -1 then stop the function and return false to indicate the function failed
		
    to_tab = GetTableByName(toTableName) # Find the from table if it exists 
    if to_tab == None: # Test if a table was found
        return False #If not then stop the function and return false to indicate the function failed

    to_tab.Lock() # Lock the table for writing, ie this allows data to be edited

    fld_to_key = CheckFieldExists(to_tab, toKey) # Find the key field index
    fld_to_value = CheckFieldExists(to_tab, toField) # find the to field index
    
    if fld_to_value == -1 or fld_to_key == -1: # test that both field exists
        return False # If one of the fields are -1 then stop the function and return false to indicate the function failed
    
    #Loop through the to table and get a matching record from the from table. If an matching key was found then copy data across.

    # Create a progress bar and set its length to the number of records in the to tbale
    prog = general.ProgressBar("Copying data from " + fromTableName + " to " + toTableName + " (" + fromField + " > " + toField + ")", to_tab.RecordCount())
    try: # Use the progress bar in a try finally as the progress bar must always close, even if there were errors
        for recordindex in range(to_tab.RecordCount()): # Loop through all the records in the to table
            if to_tab.IsRecordAlive(recordindex): # check if the to table record is alive, erased records could cause problems

                key = to_tab.GetText(fld_to_key,recordindex) # Get the to table key                                                    
                records = fr_tab.RecordsFromValue(fld_fr_key, key) # Search the from table for all records matching the to table key
                
                for index in records: # Loop through all the records matching the to table key
                    if fr_tab.IsRecordAlive(index): # check if the from table record is alive, erased records could cause problems
                        value = fr_tab.GetText(fld_fr_value,index) # Get the value at the specified record                    
                        if to_tab.SetText(fld_to_value, recordindex, value): # Set the value to the to record, if successful then break and go on to the next to table record
                            break # continue to the next to table record

            prog.Increment() # Increment the progress bar, increments for every to table record
    finally:
        prog.Close() # Close the progress bar, important step, if this is not called then the progress bar will be there forever

    # Show a notification to show the step has been completed.
    general.ShowNotification("Copied data from " + fromTableName + " to " + toTableName + " (" + fromField + " > " + toField + ")", general.AlbionMessageTypes.ntSuccess)

    return True # return true to indicate the function completed successfully


def ClearField(tableName, field):
    """
    This function clears all the values of a field in the specified table
    tableName -> The gis layer name of the table 
    filed -> Name of the field in the table that will be cleared
    """

    table = GetTableByName(tableName) # Find the table if it exists 
    if table == None:
        return False # If not found then stop the function and return False to indicate the function failed 
        
    fldIndex = CheckFieldExists(table, field) # Find the field index
    if fldIndex == -1: # test the field exists
        return False # If not found then stop the function and return False to indicate the function failed 

    table.Lock() # Lock the table for writing, ie this allows data to be edited

    for recordindex in range(table.RecordCount()): # loop through all the records in the table
        if table.IsRecordAlive(recordindex): # check if the record is alive, erased records could cause problems
            table.SetText(fldIndex, recordindex, "") # Set the field value to an empty string

    # Show a notification to show the step has been completed. 
    general.ShowNotification("Cleared field: " + field + " in table " + tableName, general.AlbionMessageTypes.ntSuccess)

    return True # return true to indicate the function completed successfully

if __name__ == "__main__":
    """
    The entry point of the function
    """

    ClearField("Wa_pipe","Name") # Clear the Name field from the Wa_Pipe layer
    ClearField("Wa_pipe","Sub_Name") # Clear the Sub_Name field from the Wa_pipe layer

    # Run the vlookups, see the vlookup function for more details
    VLookup(fromTableName="Wa_node", fromKey="Node_Code", fromField="System", toTableName="Wa_pipe", toKey="To_Code", toField="Name")  
    VLookup(fromTableName="Wa_node", fromKey="Node_Code", fromField="System", toTableName="Wa_pipe", toKey="From_Code", toField="Name")  

    VLookup(fromTableName="Wa_node", fromKey="Node_Code", fromField="System", toTableName="Wa_pipe", toKey="To_Code", toField="Sub_Name")  
    VLookup(fromTableName="Wa_node", fromKey="Node_Code", fromField="System", toTableName="Wa_pipe", toKey="From_Code", toField="Sub_Name")  

    # Refresh all rendering.
    # If this is not done the any changes might not show in the drawing/renderer
    gis.AlbionGisLayer().RefreshRendering()

    # Show a notification to show the process has been completed. 
    general.ShowNotification("Complete.", general.AlbionMessageTypes.ntShowSuccessMsg)