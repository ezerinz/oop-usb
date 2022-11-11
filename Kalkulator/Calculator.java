public class Calculator {
	double angka1;
	double angka2;
	char operasi;

	void Hitung(){
		double hasil = 0;
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
				hasil = 0;
				System.out.println("Operasi tidak terdefinisi!");
	 			break;
		}

		if(hasil != 0){
			System.out.println(angka1 + " " + operasi + " " + angka2 + " =" + " " + hasil);
		}
	}
}
