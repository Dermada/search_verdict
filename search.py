import os
import sys
import time as t

#imports folder dir
folder = os.listdir("dataset/")

#input
#memastikan input console sesuai dengan ketentuan program
if 2 < len(sys.argv) < 8 and len(sys.argv) != 4 and len(sys.argv) != 6: #input harus 3,5, atau 7 kata
    desired_section = sys.argv[1] #section yang ingin dipindai
    kata_kunci1 = sys.argv[2] #kata kunci pencarian 1
    search_filter = None
    kata_kunci2 = ""
    sort_by = None
    element_to_sort = None
    if len(sys.argv) > 4: 
        if sys.argv[3] in ["AND", "OR", "ANDNOT"]: 
            search_filter = sys.argv[3] #filter pencarian and, or, atau andnot
            kata_kunci2 = sys.argv[4] #kata kunci pencarian 2
        elif sys.argv[3] == "SORTBY":
            sort_by = sys.argv[3] #filter sorting harus "SORTBY"
            element_to_sort = sys.argv[4] #elemen menjadi dasar sorting
            if element_to_sort not in ["file_name", "provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:
                sys.exit("\nElement tidak valid, harus berupa file_name, provinsi, klasifikasi, sub_klasifikasi, atau lembaga_peradilan")
        else:
            sys.exit("\nMode harus berupa AND ,OR, ANDNOT, ATAU SORTBY") 
        if len (sys.argv) == 7:
            if sys.argv[3] != "SORTBY":
                sort_by = sys.argv[5]
                if sort_by != "SORTBY":
                    sys.exit("\nuntuk sorting harus menggunakan 'SORTBY'.")
                element_to_sort = sys.argv[6]
                if element_to_sort not in ["file_name", "provinsi", "klasifikasi", "sub_klasifikasi", "lembaga_peradilan"]:
                    sys.exit("\nElement tidak valid, harus berupa file_name, provinsi, klasifikasi, sub_klasifikasi, atau lembaga_peradilan")
            else:
                sys.exit("\nArgumen program tidak benar.")
else:
    print()
    sys.exit("\nArgumen program tidak benar.")

#necessary variables
start_section = f"<{desired_section}>" #menandandakan awal section
end_section = f"</{desired_section}>" #menandakan akhir section
documents_found = 0 #dokumen yang telah ditemukan
master_list = [] #nestedlists untuk dokumen-dokumen yang telah ditemukan
files_scanned = 0 #files yang telah dipindai

def print_docs(): #function untuk print setiap file yang ditemukan
    print(f"{'file name': >36} {'provinsi': >15} {'klasifikasi': >15} {'sub_klasifikasi': >30} {'lembaga_peradilan': >20}")
    print("-"*120) #print header
    for files in master_list:
        print(f"{files[0]: >15} {files[1]: >15} {files[2]: >15} {files[3]: >30} {files[4]: >20}")


def sort_and_print_docs(element): #fucntion untuk sort dan print setiap file yan ditemukan
    master_list.sort(key=lambda x: x[element])
    print_docs()

def append_doc(): #function untuk append file yang ditemukan ke master list
    master_list.append((file_name, provinsi, klasifikasi, sub_klasifikasi, lembaga_peradilan))
    global documents_found
    documents_found += 1
    return documents_found

print()
st = t.time() #start timer

#iterasi setiap file dalam folder
for file_name in folder:
    file_path = os.path.join("dataset/", file_name)
    with open(file_path, "r") as current_file: #open setiap file dalam folder
        
        first_line = current_file.readline()
        provinsi = first_line[first_line.find("provinsi=\"") + len("provinsi=\""):first_line.find("\" status")]
        provinsi = provinsi[:15] #mengambil elemen provinsi dan membatasinya menjadi 15 character
        klasifikasi = first_line[first_line.find("klasifikasi=\"") + len("klasifikasi=\""):first_line.find("\" lama_hukuman")]
        klasifikasi = klasifikasi[:15] #mengambil elemen klasifikasi dan membatasinya menjadi 15 character
        sub_klasifikasi = first_line[first_line.find("sub_klasifikasi=\"") + len("sub_klasifikasi=\""):first_line.find("\" url")]
        sub_klasifikasi = sub_klasifikasi[:30] #mengambil elemen sub klasifikasi dan membatasinya menjadi 30 character
        lembaga_peradilan = first_line[first_line.find("lembaga_peradilan=\"") + len("lembaga_peradilan=\""):first_line.find("\" provinsi")]
        lembaga_peradilan = lembaga_peradilan[:20] #mengambil elemen lembaga peradilan dan membatasinya menjadi 20 character
        current_file.seek(0) #agar cursor kembali ke paling awal file

        if desired_section == "all": #jika input section "all" maka akan mencari kata kunci dari semua bagian file
            section_content_list = current_file.readlines()
        
        elif desired_section != "all": #mencari kata kunci berdasarkan section yang diinginkan
            section_content_list = [] #list untuk setiap baris dalam section
            in_section = False
            for line in current_file:
                if start_section in line:
                    in_section = True #jika start section ada di line maka sudah masuk section
                elif in_section and end_section not in line:
                    section_content_list.append(line) #append semua line dalam section
                elif end_section in line:
                    break #jika end section ada di line, break
        section_content = " ".join(section_content_list).replace("\n", "") #ubah list isi section menjadi sebuaha string yang panjang

        ada_kata_kunci1 = False
        ada_kata_kunci2 = False
        if kata_kunci1 in section_content:
            ada_kata_kunci1 = True #jika ada kata kunci 1, maka variabel ada_kata_kunci1 True
        if kata_kunci2 in section_content:
            ada_kata_kunci2 = True #jika ada kata kunci 2, maka variabel ada_kata_kunci2 True
    
        if search_filter == "AND": #jika search filter adalah AND, maka harus ada kata kunci 1 dan 2
            if ada_kata_kunci1 == True and ada_kata_kunci2 == True:
                append_doc()
        elif search_filter == "OR": #jika search filter adalah OR, maka salah satu harus ada
            if ada_kata_kunci1 == True or ada_kata_kunci2 == True:
                append_doc()
        elif search_filter == "ANDNOT": #jika ANDNOT, maka kata kunci 1 harus ada dan kata kunci 2 gaboleh ada
            if ada_kata_kunci1 == True and ada_kata_kunci2 == False:
                append_doc()
        elif search_filter == None:
            if ada_kata_kunci1 == True:
                append_doc()
    files_scanned += 1 
    sys.stdout.write(f"dokumen terpindai {files_scanned}  dokukmen ditemukan {documents_found}\r") #progress tracker pemindai
end = t.time()

#sorting
if element_to_sort == "file_name":
    sort_and_print_docs(0)
elif element_to_sort == "provinsi":
    sort_and_print_docs(1)
elif element_to_sort == "klasifikasi":
    sort_and_print_docs(2)
elif element_to_sort == "sub_klasifikasi":
    sort_and_print_docs(3)
elif element_to_sort == "lembaga_peradilan":
    sort_and_print_docs(4)
elif element_to_sort == None:
    print_docs()

print()
print(f"Banyaknya dokumen yang ditemukan = {documents_found}") #docs found
print(f"Totak waktu pencarian            = {(end - st):.3f} detik") #end timer

"""
contoh input:
python search.py all 'barang bukti berupa 1 satu buah laptop' SORTBY provinsi
python search.py fakta 'kebakaran hutan' OR 'narkotika gol onga' SORTBY sub_klasifikasi
"""