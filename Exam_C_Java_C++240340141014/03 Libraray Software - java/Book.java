package com.jeet;

public class Book {
	String Book_Name, Publisher, Writer;
	float MRP;

	Book(String book_Name, String publisher, String writer, float price) {
		this.Book_Name = book_Name;
		this.Publisher = publisher;
		this.Writer = writer;
		MRP = price;
	}

}
