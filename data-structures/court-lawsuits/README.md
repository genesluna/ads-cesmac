# Data structures assignment - search optimization

When we are dealing with technology, it is common to always be looking for agility in queries. When dealing with databases, for example, whenever we perform a common query on the database, we perform a sequential linear query, in which the database will search row by row in the table for the information being sought. In a table with millions of pieces of information, this query can take several seconds, even more than a minute, which can harm sales sites such as Mercado Livre, Amazon or Americanas, since the delay in the query result can lead the customer to abandon the purchase. Therefore, it is common for databases to implement a search-optimized data structure for some types of data, such as the use of hashes or binary trees, reducing the search time to a few seconds.

Given this scenario, think of a business sector that needs to perform optimized searches. Create an example, in code format, of how using an optimized structure would make this search faster. As a guide, follow the steps below. Present the search algorithm used and how it can make the search more effective and/or the difficulties in using such resources.

- Step 1: Choose a resource from a business area that needs an optimized search and create a code that exemplifies this listing that will be optimized.
- Step 2: Create and apply the structure that allows you to perform the optimized search.

<br/>

# The strategy

## Step 01:

For the first step we chose the system of a court of law which has to deal with thousands of cases. We created a utility class that has a method that creates a certain number of processes in memory to serve as a basis for optimizations.

## Step 02:

In the second step, we performed the search using three different methods so that we could compare the results and choose the best solution for the presented problem. We used a simple sequential search to serve as a control group, a binary search performed after sorting the data and, lastly, a search in a hash table.

<br/>

# The Results

The results showed that, obviously, the worst solution is the sequential search. The further from the beginning of the list an item is, the longer it takes to find it.

In the case of binary search, when we take into account the time spent on sorting, it performs worse than sequential search. But once the data is sorted, the performance is much better.

In our specific problem, where each process has a unique identification number, the hash table won out. Although it has limitations in non-equality searches, its performance would justify its use for the presented problem.
