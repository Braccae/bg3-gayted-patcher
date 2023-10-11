
To use this class, you can do something like this:

divine = DivineWrapper()
divine.extract_package('path_to_source_file.pak', 'path_to_target_dir')
divine.create_package('path_to_source_dir', 'path_to_target_file.pak')
divine.extract_packages('path_to_source_dir', 'path_to_target_dir')


Please replace 'path_to_divine.exe', 'path_to_source_file.pak', 'path_to_target_dir', 'path_to_source_dir', and 'path_to_target_file.pak' with the actual paths on your system.

Note: This code assumes that divine.exe is in your system's PATH. If it's not, you'll need to provide the full path to divine.exe in the divineTool variable.