SELECT products.name, providers.name, products.price FROM products
INNER JOIN categories 
    ON categories.id = products.id_categories
INNER JOIN providers
    ON  providers.id = products.id_providers

WHERE categories.name = 'Super Luxury' 
AND products.price > 1000 