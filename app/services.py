products_db = []


# -----------------------------
# GET ALL PRODUCTS
# -----------------------------

def get_all_products():

    return products_db


# -----------------------------
# GET SINGLE PRODUCT
# -----------------------------

def get_single_product(product_id):

    if product_id >= len(products_db):

        return None

    return products_db[product_id]


# -----------------------------
# CREATE PRODUCT
# -----------------------------

def create_new_product(product):

    products_db.append(product.model_dump())

    return product


# -----------------------------
# UPDATE PRODUCT
# -----------------------------

def update_existing_product(product_id, product):

    if product_id >= len(products_db):

        return None

    products_db[product_id] = product.model_dump()

    return product


# -----------------------------
# DELETE PRODUCT
# -----------------------------

def delete_existing_product(product_id):

    if product_id >= len(products_db):

        return None

    return products_db.pop(product_id)