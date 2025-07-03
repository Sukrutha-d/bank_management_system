typedef struct bank{
char fname[25];
char lname[25];
char fathername[25];
char mothername[25];
int date,month,year;
int adhaarnum;
int accountno;
char acctype[25];
char address[30];
int balance;
int withdrawamt;
int depamount;
char ddate[20];
}bank;
void create_account(bank *b,int n);
void check_balance(bank *b,int n);
void deposit(bank *b,int n);
void withdraw(bank *b,int n);
void checkwith(bank *b,int n);
void display_details(bank *b,int n);
void bubble_sort(bank *b,int n);
void display_deposit_details(bank *b, int n);
#include <stdio.h>
#include <string.h>
#include <conio.h>
int main(){
char opt;
int choice;
bank b[100];
int n;
printf("Enter the number of choices:");
scanf("%d",&n);
do {
printf("\t\t\t\t\t WELCOME TO BANK MANAGEMENT SYSTEM");
printf("\n\t\t1.Create a bank account.");
printf("\n\t\t2.Check Balance.");
printf("\n\t\t3.Deposit amount.");
printf("\n\t\t4.Withdraw amount.");
printf("\n\t\t5.Check for Withdrawn amount less than 1000.");
printf("\n\t\t6.Check for the transaction details for a particular account no.");
printf("\n\t\t7.Sort based on name.");
printf("\n\t\t8.Display deposit details between particular dates.");
printf("\n\t\t9.Exit");
printf("\n\n\t\tEnter your choice:");
scanf("%d",&choice);
switch(choice){
case 1 : create_account(b,n);
printf("\nAccount created successfully.");
break;
case 2 : check_balance(b,n);
printf("\nBalance displayed.");
break;
case 3 : deposit(b,n);
printf("\nAmount deposited successfully.");
break;
case 4 : withdraw(b,n);
printf("\nAmount withdrawn successfully.");
break;
case 5 : printf("\nDisplaying the withdrawn amounts less than 1000");
checkwith(b,n);
break;
case 6 : printf("\nDisplaying the transaction details");
display_details(b,n);
break;
case 7 : printf("\nSort based on name");
bubble_sort(b,n);
break;
case 8 :
printf("\nDisplaying deposit details within a specified date range");
display_deposit_details(b, n);
break;
case 9 : printf("Thank you!");
break;
default : printf("Invalid input.");
break;
}
printf("\nDo you want to continue?(Y/N):");
scanf(" %c",&opt);
}while(opt=='y'||opt=='Y');
return 0;
}
void create_account(bank *b,int n){
char ch;
char password[13];
for(int i=1;i<n+1;i++){
printf("\nFIRST NAME:");
scanf("%s",(b+i)->fname);
printf("\nLAST NAME:");
scanf("%s",(b+i)->lname);
printf("\nFATHER NAME:");
scanf("%s",(b+i)->fathername);
printf("\nMOTHER NAME:");
scanf("%s",(b+i)->mothername);
printf("\nDOB(DD/MM/YY):");
scanf("%d/%d/%d",&(b+i)->date,&(b+i)->month,&(b+i)->year);
printf("\nADDRESS:");
scanf("%s",(b+i)->address);
printf("\nDate: ");
scanf("%s",(b+i)->ddate);
printf("\nAADHAAR NUMBER: ");
scanf("%d",&(b+i)->adhaarnum);
printf("\nACCOUNT TYPE:");
scanf("%s",(b+i)->acctype);
printf("\nACCOUNT NUMBER:");
scanf("%d",&(b+i)->accountno);
printf("\nBALANCE:");
scanf("%d",&(b+i)->balance);
printf("\nPASSWORD:");
for(int i=0;i<=10;i++){
ch=getch();
if(ch!=11){
password[i]=ch;
ch = '*';
printf("%c",ch);
}
}
if((b+i)->accountno==12345){
printf("\nAccount already exists.");
}
}
}
void check_balance(bank *b,int n){
for(int i=1;i<n+1;i++){
if((b+i)->accountno<=0){
printf("\n Account number invalid.");
}
else
printf("\nCurrent balance of account %d : %d",i,(b+i)->balance);
}
}
void deposit(bank *b,int n){
for(int i=1;i<n+1;i++){
printf("\nEnter the amount to be deposited to account %d:",i);
scanf("%d",&(b+i)->depamount);
if((b+i)->depamount<=0){
printf("\nInvalid amount.");
}
else{
(b+i)->balance=(b+i)->balance+(b+i)->depamount;
printf("\nCurrent balance:%d",(b+i)->balance);
}
}
}
void withdraw(bank *b,int n){
for(int i=1;i<n+1;i++){
printf("\nEnter the amount to withdraw from account %d:",i);
scanf("%d",&(b+i)->withdrawamt);
if((b+i)->withdrawamt>(b+i)->balance){
printf("\nInvalid amount.");
}
else{
(b+i)->balance=(b+i)->balance-(b+i)->withdrawamt;
printf("\nCurrent balance:%d",(b+i)->balance);
}
}
}
void checkwith(bank *b,int n){
for(int i=1;i<n+1;i++){
if((b+i)->withdrawamt<1000)
printf("\nwithdraw amounts are : %d",(b+i)->withdrawamt);
}
}
void display_details(bank *b,int n){
int check_acc;
printf("\nEnter the account number to display the transaction details:");
scanf("%d",&check_acc);
for(int i=1;i<n+1;i++){
if(check_acc==(b+i)->accountno){
printf("\n Balance : %d", (b+i)->balance);
printf("\n Deposited amount : %d",(b+i)->depamount);
printf("\n Withdrawn amount : %d",(b+i)->withdrawamt);
}
}
}
void bubble_sort(bank *b, int n) {
int i, j;
for (i = 0; i < n - 1; i++) {
for (j = 0; j < n - i - 1; j++) {
if (strcmp(b[j].fname, b[j + 1].fname) > 0) {
bank t=b[j-1];
b[j-1]=b[j];
b[j]=t;
}
}
}
for(int i=1;i<n+1;i++){
printf("\nFirst name : %s",(b+i)->fname);
printf("\nLast name :%s",(b+i)->lname);
printf("\nAccount number : %d",(b+i)->accountno);
}
}
void display_deposit_details(bank *b, int n) {
int acc_num;
char sdate[20];
char edate[20];
printf("\nEnter the account number to display deposit details: ");
scanf("%d", &acc_num);
printf("\nEnter the start date (DD/MM/YY): ");
scanf("%s",&sdate);
printf("\nEnter the end date (DD/MM/YY): ");
scanf("%s",&edate);
for (int i = 1;i<n+1; i++) {
if (acc_num == (b + i)->accountno) {
if((strcmp((b+i)->ddate,sdate))>=0){
if((strcmp((b+i)->ddate,edate))<=0){
printf("\nDate: %d/%d/%d - Deposit Amount: %d", (b + i)->date, (b + i)->month, (b + i)-
>year, (b + i)->depamount);
}
}
}
}
}
