"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# Answer: The returned value is an object of instances of brands with name attribute
# of "Ford".


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# Answer: Association table is a table that joins other tables in a many-to-many
# relationship. The association table does not have any meaningful fiels and can
# be thought as the glue between two tables. Columns of association tables are
# foreign keys.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').all()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter((Model.name == "Corvette") & (Model.brand_id == "che")).all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter((Brand.founded == 1903) & (Brand.discontinued == None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != "for").first()

# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    query = db.session.query(Model.name, Brand.name,
            Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for model_name, brand_name, headquarters in query:
        print model_name, ",", brand_name, ",", headquarters


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    # Querying the database to get all brand names, model names and years
    # This will output a list of tupples
    query = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()

    # Creating empty dictionary to organise data based on brand name
    query_dict = {}

    # Adding each brand name as key to dictionary and each model name and year
    # as value pairs for that brand name
    for brand_name, model_name, year in query:
        if brand_name not in query_dict:
            query_dict[brand_name] = [(model_name, year)]
        else:
            query_dict[brand_name].append((model_name, year))

    # Printing out each brand name and list of model names with year for that
    # brand
    for key in query_dict:
        print key, query_dict[key]


    # The instructions for this function were not very clear to me. I wrote the
    # above function and logic to print out brand name and all model names and
    # years for that brand

    # The loop below will print all brand names and model names and year for
    # that brand.
    # for brand_name, model_name, year in query:
    #     print brand_name, ",", model_name, ",", year


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    query_brand = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()

    return query_brand


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    query_model = Model.query.filter((Model.year >= start_year) &
                                     (Model.year < end_year)).all()

    return query_model
