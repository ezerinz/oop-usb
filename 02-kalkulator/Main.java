/* Nama: Edwin
 * NIM: D0221371
 * Kelas: Informatika H 
 */

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		
		//scanner
		Scanner input = new Scanner(System.in);

		//panggil kalkulator class
		Calculator kalkulator = new Calculator();
		
		while(true){
			System.out.print("Masukkan Angka Pertama: ");
			kalkulator.angka1 = input.nextDouble();

			System.out.print("Masukkan Angka Kedua: ");
			kalkulator.angka2 = input.nextDouble();

			System.out.println("+ (Penjumlahan)");
			System.out.println("- (Pengurangan)");
			System.out.println("* (Perkalian)");
			System.out.println("/ (Pembagian)");
			System.out.print("Pilih Operasi: ");
			kalkulator.operasi = input.next().charAt(0);

			kalkulator.Hitung();
			

			System.out.print("Berhenti? (Y/N): ");
			char stop = input.next().charAt(0);
			if(stop == 'Y'){
				break;
			}

		}
	}
}

