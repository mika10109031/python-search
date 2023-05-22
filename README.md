# python-search
Dalam Percobaan Binary Search_Rotation,
Menemukan rotasi terkecil dalam sebuah list yang sudah dirotasi. Kita mulai dengan menentukan low (indeks pertama dalam daftar) dan high (indeks terakhir dalam daftar). Dalam loop while, kita menghitung indeks tengah (mid) dengan menggunakan operator floor division // pada penjumlahan low dan high. Kita membandingkan elemen yang berada di indeks mid dengan elemen yang berada di indeks high. Jika data[mid] lebih besar dari data[high], itu berarti titik rotasi berada di sebelah kanan mid. Oleh karena itu, kita perbarui low = mid + 1 untuk mencari di sebelah kanan mid. Jika data[mid] tidak lebih besar dari data[high], itu berarti titik rotasi berada di sebelah kiri mid atau mid itu sendiri adalah indeks rotasi terkecil. 
Dalam Percobaan Binary Search_Most Frequent,
Menemukan elemen yang sering muncul paling banyak dalam sebuah list yang sudah diurutkan. Variabel max_count digunakan untuk melacak jumlah kemunculan maksimum dari elemen yang paling sering muncul.Variabel most_frequent digunakan untuk menyimpan elemen yang paling sering muncul.Kita mulai dengan menentukan low (indeks pertama dalam daftar) dan high (indeks terakhir dalam daftar).Dalam loop while, kita menghitung indeks tengah (mid) dengan menggunakan operator floor division // pada penjumlahan low dan high.Kita inisialisasi count dengan 1 untuk menghitung jumlah kemunculan elemen di indeks mid.Kita periksa elemen-elemen di sebelah kiri dan kanan mid untuk menghitung jumlah kemunculan yang sama
Dalam Percobaan Binary Search_Name List,
Mencari data dalam list terurut. Pertama, kita menentukan low sebagai indeks pertama dalam daftar dan high sebagai indeks terakhir dalam daftar.
Jika elemen di indeks mid sama dengan target yang dicari, maka kita langsung mengembalikan nilai mid sebagai indeks yang sesuai.Jika elemen di indeks mid lebih kecil dari target, artinya target berada di sebelah kanan mid. Oleh karena itu, kita perbarui low = mid + 1 untuk mencari di sebelah kanan mid.Jika elemen di indeks mid lebih besar dari target, artinya target berada di sebelah kiri mid. Dalam kasus ini, kita perbarui high = mid - 1 untuk mencari di sebelah kiri mid.Loop while akan terus berlanjut selama low kurang dari atau sama dengan high
