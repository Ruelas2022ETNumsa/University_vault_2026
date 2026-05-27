------


```javascript
#define Led_R
#define Led_B
#define Led_G

void F_signo(int n){
	Serial.println("\n\t\a El nuemro es :");
	Serial.println(n);
	if(n==0){
		digitalWrite(Led_R, HIGH);
		delay(1000);
		digitalWrite(Led_R, LOW);
		delay(1000);
	}
	else if(n<=1){
		digitalWrite(Led_G, HIGH);
		delay(1000);
		digitalWrite(Led_G, LOW);
		delay(1000);
	}
	else{
		digitalWrite(Led_B, HIGH);
		delay(1000);
		digitalWrite(Led_B, LOW);
		delay(1000);
	}
}

void setup() {
	Serial.begin(9600);
	pinMode(Led_R, OUTPUT);
	pinMode(Led_B, INPUT);
	pinMode(Led_G, OUTPUT);
	Serial.println("\n\t\a Ingresar un numero inetero :");
}

void loop() {
	if(Serial.available()){
	    string cad;
	    cad = Serial.readString();
	    F_signo(cad.toint());
	}
}

```


```javascript
#define Led_R D6
#define Led_B D7
#define Led_G D8

void setup(){
	Serial.begin(9600);
	pinMode(Led_R, OUTPUT);	pinMode(Led_B, OUTPUT); 	pinMode(Led_G, OUTPUT);
	Serial.println("\n\t Ingresar un numero entero :");
}

void loop(){
	if(Serial.available()){
	    String cad;
	    cad = Serial.readString();
	    cad.toInt(n);
	    
		Serial.print("\n\t El numero ' ");	Serial.print(n);Serial.print(" ' es ");
		
		digitalWrite(Led_R, LOW); digitalWrite(Led_B, LOW); digitalWrite(Led_G, LOW);
		
		if(n==0){
			digitalWrite(Led_R, HIGH);
		    Serial.println(" CERO.");
		}
		else if(n<0){
			digitalWrite(Led_B, HIGH);
		    Serial.print(" NEGATIVO.");
		}
		else if(n>0){
			digitalWrite(Led_G, HIGH);
		    Serial.println(" POSITIVO.");
		}
		else{
		    Serial.println("error");
		}
	}
}

```