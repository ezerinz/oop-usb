/* Nama: Edwin
 * NIM: D0221371
 * Kelas: Informatika H 
 */

public class Calculator {
	double angka1;
	double angka2;
	char operasi;

	
	void Hitung(){
		double hasil = 0;
		boolean adaHasil = true;
		switch (operasi) {
			case '+':
				hasil = angka1 + angka2;
				break;
			case '-':
				hasil = angka1 - angka2;
				break;
			case '*':
				hasil = angka1 * angka2;
				break;
			case '/':
				hasil = angka1 / angka2;
				break;
			default:
				adaHasil = false;
				System.out.println("Operasi tidak terdefinisi!");
	 			break;
		}

		if(adaHasil != false){
			System.out.println(angka1 + " " + operasi + " " + angka2 + " =" + " " + hasil);
		}
	}
}
