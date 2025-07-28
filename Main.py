from pbxproj import XcodeProject

def DecodeFiles():
    # Load the Xcode project
    project = XcodeProject.load('MyApp.xcodeproj/project.pbxproj')

    # Iterate over all PBXFileReference objects
    for ref in project.objects.get_objects_in_section('PBXFileReference'):
        uuid = ref.get_id()
        name = ref.get('name', '—')
        path = ref.get('path', '—')
        source_tree = ref.get('sourceTree', '—')
        file_type = ref.get('explicitFileType') or ref.get('lastKnownFileType') or '—'

        print(f"--- PBXFileReference [{uuid}] ---")
        print(f"Name         : {name}")
        print(f"Path         : {path}")
        print(f"Source Tree  : {source_tree}")
        print(f"File Type    : {file_type}")
        print()
#-------------------------------
def main():
    DecodeFiles()
#----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
