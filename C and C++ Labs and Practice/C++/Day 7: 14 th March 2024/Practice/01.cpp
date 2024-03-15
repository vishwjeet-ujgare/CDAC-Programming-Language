/*
Define a class to represent a bank account. Include the following
members: Data members
    1. Name of the depositor
    2. Account number
    3. Type of account
    4. Balance amount in the account
Member functions
    1. To assign initial values
    2 . To deposit an amount
    3. To withdraw an amount after checking the balance
    4. To display name and balance
Write a main program to test the program.
*/

#include <iostream>
#include <string>

using namespace std;

class BankAcoount
{
public:
    string name;
    string accNum;
    string accType;
    double balance = 0.0;
    double depositAmt = 0.0;
    double withdraw = 0.0;
    

    // Constructor to assign initial values
    void BankAccount(string name, string accType, long accNum, double intialBalance)
    {
        this->name = name;
        this->accType = accType;
        this->accNum = accNum;
    }

    // function to deposit an amount)

    void deposite(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
            cout << "Deposit Succesful of amount " << amount << endl;
        }
        else
        {
            cout << "invalid amount for deposite " << endl;
        }
    }

    // withdrawl function

    void withdrawl(double amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;

            cout << "deposite withdraw for " << amount << endl;
        }
    }

    void remaingBalance()
    {
        cout << "Available balance is : " << balance;
    }

    // disply name name balace
    void display()
    {

        cout << "account holder" << name << endl;
        cout << "balance :" << balance << endl;
    }
};

int main()
{
    BankAcoount b;

    // cout<<"Enter bank A/c details "<<endl;

    // cout<<"Enter A/c holder name : ";
    // cin>>b.name;

    // cout<<"Enter A/c number : ";
    // cin>>b.accNum;

    // cout<<"Enter A/c type : ";
    // cin>>b.accType;

    cout << "Enter Amount to deposit : ";
    cin >> b.depositAmt;

    b.deposite(b.depositAmt);

    cout << endl;
    cout << "Enter Amount for withdrawal money : ";
    cin >> b.withdraw;

    b.withdrawl(b.withdraw);

    cout << endl;
    b.remaingBalance();
}
