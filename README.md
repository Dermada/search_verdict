# Search Engine for a Dataset of Court Decisions
This is a Python program for searching and filtering documents in a given directory based on specific keywords and sections within the documents. It can also perform sorting on the search results.

## Acknowledgements
This search engine is targeted only for a dataset provided by Nuranti, E.Q., Yulianti, E., & Husin , H.S. for their master's thesis at the Faculty of Computer Science,
University of Indonesia (Fasilkom UI).

Link to the original dataset:
https://github.com/ir-nlp-csui/indo-law/tree/main

You can learn more about this dataset by referring to the following thesis:
Nuranti, E. Q., Yulianti, E., & Husin, H. S. (2022). Predicting the Category and the Length of Punishment in Indonesian Courts Based on Previous Court Decision Documents. Computers, 11(6), 88.

## Usage
The program could only run for the dataset mentioned in the Acknowledgements sub-section  
The program should be run from the command line. It accepts the following arguments:
```xml
python search.py [desired_section] [kata_kunci1] [search_filter] [kata_kunci2] SORTBY [element_to_sort]
```
| No. | Arguments | Description |
| --- | --- | --- |
| 1. | **desired_section** | The section within the documents to search for keywords. Use "all" to search in all sections.  
| 2. | **kata_kunci1** | The first keyword to search for within the specified section.  
| 3. | **search_filter** | Optional. Use "AND", "OR", or "ANDNOT" to specify how the keywords should be filtered.  
| 4. | **kata_kunci2** | Optional. The second keyword to search for when using "AND", "OR", or "ANDNOT" search filters.  
| 5. | **SORTBY** | Use "SORTBY" to specify sorting.  
| 6. | **element_to_sort** | The element by which to sort the search results. Options are "file_name," "provinsi," "klasifikasi," "sub_klasifikasi," or "lembaga_peradilan."  

## Example Usages
Search in all sections for the keyword "barang bukti berupa 1 satu buah laptop" and sort by "provinsi":
```xml
python search.py all 'barang bukti berupa 1 satu buah laptop' SORTBY provinsi
```
Search in the "fakta" section for "kebakaran hutan" or "narkotika gol onga" and sort by "sub_klasifikasi":
```xml
python search.py fakta 'kebakaran hutan' OR 'narkotika gol onga' SORTBY sub_klasifikasi
```

## Output
The program will display the documents that match the search criteria, including file name, provinsi, klasifikasi, sub_klasifikasi, and lembaga_peradilan.

## Sorting
The program allows you to sort the search results by specifying the element you want to use as the sorting criteria. If sorting is not specified, the program will display the results in the order they were found.

## Author
This program was created by Dermada@github.

## License
This project is licensed under GNU General Public License 3.0  
for more details, please check the license file:
https://github.com/Dermada/search_verdict/blob/889d5b39491b4c9023300640b68cd8ab8c625dea/LICENSE
