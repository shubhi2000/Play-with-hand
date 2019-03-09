void setup(){
 Serial.begin(9600); 
 pinMode(2,INPUT);
}
int f=0;
void loop(){
  int a=digitalRead(2);
  if(a==HIGH){ f++; delay(2000);}
  if(f%2!=0){
  int f0=analogRead(A0);
  int g0=analogRead(A1);
  delay(1000);
  int f1=analogRead(A0);
  int g1=analogRead(A1);
  delay(1000);
  int f2=analogRead(A0);
  int g2=analogRead(A1);
  /*Serial.print(f0);
  Serial.print("\t");
  Serial.println(g0);*/
  if (f0<=750 && f1<=750 && f2<=750){
   if (g0<=750 && g1<=750 && g2<=750)
      Serial.println("Select");
   else 
      Serial.println("Back");
  }
  else{
    if (g0<=750 && g1<=750 && g2<=750)
      Serial.println("Down");
   else 
      Serial.println("Up");
  }
  }
}
