select author.author_id, author.author_name, book.category, sum(book_sales.sales*book.price) as total_sales
from book, author, book_sales
where book.book_id=book_sales.book_id
and book.author_id=author.author_id
and sales_date like '2022-01%'
group by  author.author_id, author.author_name, book.category
order by author.author_id, category desc