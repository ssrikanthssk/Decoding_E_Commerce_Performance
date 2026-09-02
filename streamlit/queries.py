def get_business_overview():
    return """
        SELECT 
            (SELECT SUM(price + freight_value) FROM order_items) AS total_revenue,
            (SELECT COUNT(DISTINCT order_id) FROM orders) AS total_orders,
            (SELECT COUNT(DISTINCT customer_id) FROM customers) AS total_customers,
            (SELECT COUNT(DISTINCT seller_id) FROM sellers) AS total_sellers,
            (SELECT AVG(price + freight_value) FROM order_items) AS avg_order_value,
            (SELECT AVG(review_score) FROM order_reviews) AS avg_review_score
    """

def get_monthly_revenue_trend():
    return """
        SELECT DATE_FORMAT(o.order_purchase_timestamp, '%%Y-%%m') AS month,
               SUM(oi.price + oi.freight_value) AS revenue
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY month
        ORDER BY month
    """

def get_revenue_by_category():
    return """
        SELECT p.product_category_name, SUM(oi.price + oi.freight_value) AS revenue
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY revenue DESC
        LIMIT 15
    """

def get_top_selling_products():
    return """
        SELECT oi.product_id, COUNT(*) AS units_sold, SUM(oi.price) AS total_sales
        FROM order_items oi
        GROUP BY oi.product_id
        ORDER BY units_sold DESC
        LIMIT 10
    """

def get_sales_by_location():
    return """
        SELECT c.customer_state, SUM(oi.price + oi.freight_value) AS revenue
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY c.customer_state
        ORDER BY revenue DESC
    """

def get_customer_distribution():
    return """
        SELECT customer_state, COUNT(*) AS customer_count
        FROM customers
        GROUP BY customer_state
        ORDER BY customer_count DESC
    """

def get_customer_spending():
    return """
        SELECT o.customer_id, SUM(oi.price + oi.freight_value) AS total_spending
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY o.customer_id
    """

def get_repeat_vs_new():
    return """
        SELECT 
            CASE WHEN order_count > 1 THEN 'Repeat' ELSE 'New' END AS customer_type,
            COUNT(*) AS customer_count
        FROM (
            SELECT customer_id, COUNT(order_id) AS order_count
            FROM orders
            GROUP BY customer_id
        ) t
        GROUP BY customer_type
    """

def get_top_customers():
    return """
        SELECT o.customer_id, SUM(oi.price + oi.freight_value) AS total_spending
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY o.customer_id
        ORDER BY total_spending DESC
        LIMIT 10
    """

def get_top_sellers():
    return """
        SELECT oi.seller_id, SUM(oi.price + oi.freight_value) AS seller_revenue,
               COUNT(DISTINCT oi.order_id) AS order_count
        FROM order_items oi
        GROUP BY oi.seller_id
        ORDER BY seller_revenue DESC
        LIMIT 10
    """

def get_category_performance():
    return """
        SELECT p.product_category_name, COUNT(*) AS units_sold,
               SUM(oi.price) AS total_sales
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        GROUP BY p.product_category_name
        ORDER BY total_sales DESC
        LIMIT 15
    """

def get_seller_ratings():
    return """
        SELECT oi.seller_id, AVG(r.review_score) AS avg_rating, COUNT(*) AS review_count
        FROM order_items oi
        JOIN order_reviews r ON oi.order_id = r.order_id
        GROUP BY oi.seller_id
        HAVING review_count >= 10
        ORDER BY avg_rating DESC
        LIMIT 10
    """

def get_avg_delivery_time():
    return """
        SELECT AVG(DATEDIFF(order_delivered_customer_date, order_purchase_timestamp)) AS avg_delivery_days
        FROM orders
        WHERE order_delivered_customer_date IS NOT NULL
    """

def get_ontime_vs_delayed():
    return """
        SELECT 
            CASE WHEN order_delivered_customer_date > order_estimated_delivery_date 
                 THEN 'Delayed' ELSE 'On-Time' END AS delivery_status,
            COUNT(*) AS order_count
        FROM orders
        WHERE order_delivered_customer_date IS NOT NULL
        GROUP BY delivery_status
    """

def get_delivery_by_location():
    return """
        SELECT c.customer_state, 
               AVG(DATEDIFF(o.order_delivered_customer_date, o.order_purchase_timestamp)) AS avg_delivery_days
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        GROUP BY c.customer_state
        ORDER BY avg_delivery_days DESC
    """

def get_delay_vs_review():
    return """
        SELECT 
            CASE WHEN o.order_delivered_customer_date > o.order_estimated_delivery_date 
                 THEN 'Delayed' ELSE 'On-Time' END AS delivery_status,
            AVG(r.review_score) AS avg_review_score
        FROM orders o
        JOIN order_reviews r ON o.order_id = r.order_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        GROUP BY delivery_status
    """

def get_review_score_distribution():
    return """
        SELECT review_score, COUNT(*) AS count
        FROM order_reviews
        GROUP BY review_score
        ORDER BY review_score
    """

def get_reviews_by_category():
    return """
        SELECT p.product_category_name, AVG(r.review_score) AS avg_review_score
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        JOIN order_reviews r ON oi.order_id = r.order_id
        GROUP BY p.product_category_name
        ORDER BY avg_review_score DESC
        LIMIT 15
    """

def get_rating_vs_delivery():
    return """
        SELECT r.review_score, 
               AVG(DATEDIFF(o.order_delivered_customer_date, o.order_purchase_timestamp)) AS avg_delivery_days
        FROM orders o
        JOIN order_reviews r ON o.order_id = r.order_id
        WHERE o.order_delivered_customer_date IS NOT NULL
        GROUP BY r.review_score
        ORDER BY r.review_score
    """