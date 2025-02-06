#Real Estate Listing Platform Documentation
Overview
The Real Estate Listing Platform is a Django-based web application designed to connect buyers and sellers in the real estate market. The platform allows sellers to list their properties, while buyers can search for, filter, and purchase these listings. The system features role-based access control, ensuring that sellers and buyers have distinct permissions. Additionally, a cart system allows buyers to add properties to their cart and proceed with purchases.

Key Features
1. User Authentication
Roles: The platform includes two primary user roles:
Sellers: Can list properties, update listings, and manage their listings.
Buyers: Can browse properties, search/filter listings, and add properties to their cart.
Role-Based Access Control: Depending on the role, users have different access to features.
2. Property Listings
Sellers can add new listings with detailed information about the property, including:
Title, description, price, and property type.
Property images (upload feature).
Address and other relevant information.
Buyers can view these listings and use search and filter functionality.
3. Advanced Search & Filtering
Buyers can filter listings by various parameters such as:
Price range, property type (apartment, house, etc.).
Location (city, neighborhood, etc.).
Number of rooms, size, etc.
4. Secure Messaging
Buyers and sellers can communicate securely through a built-in messaging system.
All messages are encrypted to protect user privacy.
5. Cart System
Buyers can add properties to their cart for potential purchase.
The cart system tracks the properties selected by buyers and helps in the checkout process.
6. Admin Dashboard
Admin users can:
Manage users (create, update, delete).
Monitor and manage property listings.
Approve or reject property listings submitted by sellers.
View and manage buyer orders and transactions.
7. Role-Based Access Control
The platform features differentiated user permissions:
Sellers: Can list properties, update listings, and manage their profiles.
Buyers: Can browse properties, search listings, and communicate with sellers.
Admins: Have full access to manage users, properties, and orders.
