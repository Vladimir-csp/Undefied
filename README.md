# Undefied
Universal Desktop Entry File Editor (concept)

This is a concept of a XDG Desktop Entry editor that is based on a simple principle: exposing the underlying spec and capabilities it provides in a straightforward way.

It would consist of two components:
1. The entry editor itself, which would provide means to edit/add/remove fields to a desktop entry.
2. XDG structure editor, which would expose presense of and relations between entries scattered throughout various XDG hierarchies: Applications, Autostart, Directories.

![](https://github.com/Vladimir-csp/Undefied/blob/master/Undefied_concept.png)

Entry editor would be generic-purpose. Important known fields might have some hints and helpers, all known fields would be listed for choosing from when adding, custom fields could be added manually.
CLI arguments could be used to open editor with pre-filled fields (this would make possible to make entries based on pre-existing data, like placing a link entry to some file/directory on the desktop)

XDG structure editor would provide the ability to display entries of applications, autostart applications and desktop directories. and allow to:
- Edit entry (in most common case copy system level entry to user level and edit it in the editor)
  - Have some simple actions like hiding exposed right away without entry editor
- Put entries to system level or edit them in place (Administrative action)
- Copy entries from application hierarchy to autostart hierarchy.
- Most importatnly, expose the overrides graphically.
