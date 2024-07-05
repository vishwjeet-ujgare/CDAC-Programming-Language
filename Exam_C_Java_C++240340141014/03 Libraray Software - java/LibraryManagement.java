package com.jeet;

import java.util.*;

public class LibraryManagement {

	static ArrayList<Book> books = new ArrayList<Book>();

	public static void main(String[] args) {
		int choice;

		Scanner scan = new Scanner(System.in);

		while (true) {
			
			System.out.println("\n\n*****************");
			System.out.println("1. Save Book");
			System.out.println("2. Display all saved books");
			System.out.println("3. Exit");
			System.out.println("*****************");
			System.out.print("Enter your choice: ");

			choice = scan.nextInt();

			if (choice == 1) {
				System.out.println("-----Enter book details:---");

				
			
				System.out.print("Book Name: ");
				scan.nextLine();
				String bookName = scan.nextLine();
				
				
				System.out.print("publisher: ");
				String publisher = scan.nextLine();

				System.out.print("writer: ");
				String writer = scan.nextLine();

				System.out.print("Book MRP: ");
				float price = scan.nextFloat();

				Book newBook = new com.jeet.Book(bookName, publisher, writer, price);
				books.add(newBook);

			} else if (choice == 2) {
				int srno=0;
				for (Book book : books) {
					System.out.println((srno+1)+". "+"Book Name : " + book.Book_Name + ", Publisher: " + book.Publisher + ", "
							+ book.Writer + ", " + book.MRP);
				}
			} else if (choice == 3) {
				break;
			} else {
				System.out.println("Invalid choice. Please choose a valid option.");
			}
		}

		scan.close();
	}
}