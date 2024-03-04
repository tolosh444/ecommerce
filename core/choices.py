
# Product class size choice
SIZE_CHOICE = (
    ("XS", "XS"),
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
)

# Order class status choice

STATUS_CHOICES = (
    ('BASKET', 'Created'),
    ('PAYED', 'Payed'),
    ('ON_WAY', 'On Way'),
    ('DONE', 'Delivered'),
)

PRICE_CURRENCY = (
    ('$', 'USD'),
    ('₼', 'AZN'),
    ('€', 'EUR'),

)

COUNTRY_CHOICES = (
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AR', 'Argentina'),
    ('AU', 'Australia'),
    ('AT', 'Austria'),
    ('BE', 'Belgium'),
    ('BR', 'Brazil'),
    ('CA', 'Canada'),
    ('CN', 'China'),
    ('CO', 'Colombia'),
    ('HR', 'Croatia'),
    ('EG', 'Egypt'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('GR', 'Greece'),
    ('IN', 'India'),
    ('IT', 'Italy'),
    ('JP', 'Japan'),
    ('MX', 'Mexico'),
    ('NL', 'Netherlands'),
    ('NZ', 'New Zealand'),
    ('NO', 'Norway'),
    ('RU', 'Russia'),
    ('ZA', 'South Africa'),
    ('ES', 'Spain'),
    ('SE', 'Sweden'),
    ('CH', 'Switzerland'),
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('UY', 'Uruguay'),

)

COLOR_CHOICES = (
    ('Blue', 'Blue'),
    ('Red', 'Red'),
    ('Yellow', 'Yellow'),
    ('Green', 'Green'),
    ('Brown', 'Brown'),
    ('Pink', 'Pink'),
    ('White', 'White'),
    ('Black', 'Black'),

)
RATING_CHOICES =(
    (1,'1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)