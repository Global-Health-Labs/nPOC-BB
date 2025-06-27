# Firmware v3.x Design Updates

## Version Summary

The version summary table ([.csv](../tables/naatos_modules_fw_v3_versionsummary.csv)) lists the updates made in the minor revisions of firmware v3.

{{ read_csv("docs/tables/naatos_modules_fw_v3_versionsummary.csv", na_filter = False) }}

## Conditions

The conditions table ([.csv](../tables/naatos_modules_fw_v3_conditions.csv)) lists the status checks, performed in standby and prior to a run, that ensure a unit is healthy and able to complete a run. Last updated in firmware v3.5.

- Conditions that allow "start run"
    - Check failure causes solid yellow [notification](../outputs/notifications.md) in standby
    - Stored in `conditions_for_run` bitfield struct union
- Conditions that declare "unit ok"
    - Check failure causes fast flashing yellow/purple [notification](../outputs/notifications.md) in standby
    - Stored in `conditions_for_machine` bitfield struct union

{{ read_csv("docs/tables/naatos_modules_fw_v3_conditions.csv", na_filter = False) }}

## Errors

The errors table ([.csv](../tables/naatos_modules_fw_v3_errors.csv)) lists the reasons a run would abort before successful completion. Last updated in firmware v3.5.

{{ read_csv("docs/tables/naatos_modules_fw_v3_errors.csv", na_filter = False) }}

## Commands

The commands table ([.csv](../tables/naatos_modules_fw_v3_commands.csv)) lists the USB CDC Serial Commands.

!!! note
    The comma after many of these commands is important! The string parser won't treat them as commands with that trailing comma (on commands that don't take arguments).

{{ read_csv("docs/tables/naatos_modules_fw_v3_commands.csv", na_filter = False) }}

## Git Log

The git log ([.csv](../tables/naatos_modules_fw_v3_gitlog.csv)) lists the history of git commits made after the update to firmware v3. The log was generated using the command:

`git log --since='02-11-2025 9:00AM' --pretty=format:"%H,%ad,%an,%ae,%x22%(decorate:prefix=,suffix=,)%x22,%x22%s%x22" --date=format:"%Y-%m-%d %H:%M:%S" --reverse > gitlog.csv`

{{ read_csv("docs/tables/naatos_modules_fw_v3_gitlog.csv", na_filter = False) }}
