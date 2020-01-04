# Merge-File
This is a Python script for combining csv files in order to create a comprehensive file that is the merge of the two original files.
The script will work on both categorical and numerical data.

To do this, all column headers in the two files are read and a list is made that contains all headers with no duplications. 
This list of column headers is then written into a new file.

Next, each row identifier is written into a list with no duplications. 
This is similar to the way your column list was created in the previous step.
The row identifier list is combined into the column header file.

I work with research patient data, so my row identifiers are in the form of 'PatientID' and 'Timepoint.' 

Therefor my row identifier list is a list of tuples of all 'PatientID, Timepoint' pairs.
In your situation this is probably different. Instead of 'PatientID', you might have 'Sample', or 'Customer' or anything really. 
Also, you might have 'Date' instead of 'Timepoint.'
If that is the case, then find and replace 'PatientID' and 'Timepoint' with your specific row identifier and date/number.

The file with your unique column names and unique row identifiers is then appended with all of the original data.
When there are duplicated data points the merge will produce an average for numerical data.
When there are differences in categorical data, the merge will use the 2nd file's categorical data. 
This means that the 2nd file is assumed to be an update of the original data.

In the end the final file is a comprehensive combination of the original two files, which means it is a sort of 'Poor Man's Database.'
There should not be duplicated data anywhere in the file and no data from either of the original files is discarded.
I've used this script iteratively with many files to create a giant superfile/database of many different data types.
