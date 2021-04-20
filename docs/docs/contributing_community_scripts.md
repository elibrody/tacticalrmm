## Script Library Naming Conventions

### File names 

Under `/scripts` should generally follow this format:

```
(Platform)_(Category or Function)_(What It Does).xxx
```

!!!info
    Although Tactical RMM only has a Windows agent for now, we're planning for future with script names

Platform for now are

```
Win
OSX
Linux
iOS
Android
```


Good filename examples include:

```
Win_Azure_Mars_Cloud_Backup_Status.ps1
Win_AzureAD_Check_Connection_Status.ps1
Win_Network_DHCP_Set.bat
Win_Network_DNS_Set_to_1.1.1.2.ps1
```

!!!info
    This is so that at a glance you can see if there is already a script with that function, and you can avoid duplication of functionality. If you can improve a script or allow Script Arguments/Parameters update existing if possible

### Name field (in community_scripts.json)

Consider they are viewed in 3 different locations:

Script Manager

    - List View (sortable by any column)

    - Folder View (Grouped by Categories)

 Running scripts manually or adding tasks (or adding in Automation Manager)

!!!info
    A good max length is 50-60 chars or less for display in these 3 locations

Make sure your Name roughly follows the order of file naming as above

```
Category or Function - What It Does
```

 Consider how the alphabetic sort will affect display

![json_name_examples](images/community_scripts_name_field_example1.png)

## Script Files

### Good Habits

Try and make them fully self-contained. 

If they pull data from elsewhere, create comment notes at the top with references for others to audit/validate

Good folder locations
```
c:\ProgramData\TacticalRMM\
c:\ProgramData\TacticalRMM\scripts
c:\ProgramData\TacticalRMM\toolbox
c:\ProgramData\TacticalRMM\logs
c:\ProgramData\TacticalRMM\temp
c:\ProgramData\TacticalRMM\
```

Command Parameters are good. Optional command parameters for extra functions are better

### Bad Habits

Assumes non-standard configurations

Doesn't play well with other community scripts (reused names etc.)


## Useful Reference Script Examples

RunAsUser
[https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_Display_Message_To_User.ps1](https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_Display_Message_To_User.ps1)

Command Paramater Ninja
[https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_ScreenConnectAIO.ps1](https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_ScreenConnectAIO.ps1)

Optional Command Parameters and testing for errors
[https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_Rename_Computer.ps1](https://github.com/wh1te909/tacticalrmm/blob/develop/scripts/Win_Rename_Computer.ps1)


