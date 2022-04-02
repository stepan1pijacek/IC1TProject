#include <stdio.h>
#include <string.h>

void main(int argc, char** argv)
{
	printf("  /$$$$$$ /$$$$$$$$ /$$$$$$ /$$   /$$/$$$$$$$ /$$$$$$$$       /$$$$$$$  /$$$$$$ /$$   /$$/$$   /$$/$$$$$$/$$   /$$ /$$$$$$ \n");
	printf(" /$$__  $| $$_____//$$__  $| $$  | $| $$__  $| $$_____/      | $$__  $$/$$__  $| $$$ | $| $$  /$$|_  $$_| $$$ | $$/$$__  $$\n");
	printf("| $$  \\__| $$     | $$  \\__| $$  | $| $$  \\ $| $$            | $$  \\ $| $$  \\ $| $$$$| $| $$ /$$/  | $$ | $$$$| $| $$  \\__/\n");
	printf("|  $$$$$$| $$$$$  | $$     | $$  | $| $$$$$$$| $$$$$         | $$$$$$$| $$$$$$$| $$ $$ $| $$$$$/   | $$ | $$ $$ $| $$ /$$$$\n");
	printf(" \\____  $| $$__/  | $$     | $$  | $| $$__  $| $$__/         | $$__  $| $$__  $| $$  $$$| $$  $$   | $$ | $$  $$$| $$|_  $$\n");
	printf(" /$$  \\ $| $$     | $$    $| $$  | $| $$  \\ $| $$            | $$  \\ $| $$  | $| $$\\  $$| $$\\  $$  | $$ | $$\\  $$| $$  \\ $$\n");
	printf("|  $$$$$$| $$$$$$$|  $$$$$$|  $$$$$$| $$  | $| $$$$$$$$      | $$$$$$$| $$  | $| $$ \\  $| $$ \\  $$/$$$$$| $$ \\  $|  $$$$$$/\n");
	printf(" \\______/|________/\\______/ \\______/|__/  |__|________/      |_______/|__/  |__|__/  \\__|__/  \\__|______|__/  \\__/\\______/\n");
	
	char sys_pwd[6] = "pass";
	int accountBalance = -167495;
	int toPay = 0;
	char accountToPay[6];
	int authorized = 0;		//exploitable via overwrite this variable
	char usr_pwd[6];
	char username[128];
	
	strncpy(username, argv[1], 127);
	printf("Please login with password for user ");
	printf(username);
	printf("\nType your password:");
	scanf("%s", &usr_pwd);

	if (strcmp(usr_pwd, sys_pwd))
	{
		printf("Wrong password!\n");
	}
	else
	{
		printf("Authorized!\n");
		authorized = 1;
	}

	if (authorized)
		printf("Welcome to your bank account.\nYou have %d$ on your account.\n", accountBalance);		//test print of succeed exploit or right password
	else
		return;

	if (accountBalance < 0)
		printf("Please pay your debt or Dimitrij will knock/kick off the door :)\n");

	printf("Enter the account number for sending money:");
	scanf("%s", &accountToPay);
	printf("Enter the amount to pay:");
	scanf("%d", &toPay);
	accountBalance -= toPay;
	printf("Remains %d$\n", accountBalance);
	return;
}
