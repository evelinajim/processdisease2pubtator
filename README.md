# processdisease2pubtator
This project will read in the disease2puptator files which has associations with articles and disease. Since we are trying to filter out the articles that have cancer-related associations, we read in the MeshTreeHierarchyWithScopeNotes file and create a dictionary that finds the cancer tree id and meshID. Then we filter out the pmID files that are associated with the meshID files to get our results file. In order for this program to work you must reference the disease2pubtator file, meshtree file, and the file you want to write out the results to. It also has the option of flagging whether you want the results to contain C04 or not.


* Command line should have MeshTreeScopNotes path, disease2pubtator path, the path and file name you want to write out to, and the flag --types or -t to specify whether the user wants the corresponding MeshID to correspond to C04 exactly. If not, they can type no-C04. If none is flagged, it will automatically run the C04 one.
* example: "C:\Users\user\Pictures\Independent Study\MeshTreeHierarchyWithScopeNotes.txt" "C:\Users\user\Pictures\Independent Study\disease2pubtator.txt" "C:\Users\user\Pictures\Independent Study\test.txt" --types no-C04
* example: "C:\Users\user\Pictures\Independent Study\MeshTreeHierarchyWithScopeNotes.txt" "C:\Users\user\Pictures\Independent Study\disease2pubtator.txt" "C:\Users\user\Pictures\Independent Study\test.txt" -t C04
* The results should end up looking like one of the text files in this repository: C04.txt or no-C04.txt
