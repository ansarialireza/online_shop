from django.db import models
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext as _



class Image(models.Model):
    image = models.ImageField(upload_to='product_images/', verbose_name='تصویر')
    image_number = models.PositiveIntegerField(verbose_name='شماره تصویر')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return f"Image {self.image_number}"

class Category(MPTTModel):

    category_name = models.CharField(max_length=200, unique=True, verbose_name='نام دسته')
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', db_index=True)
    slug = AutoSlugField(populate_from='category_name', unique=True)

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    class MPTTMeta:
        order_insertion_by = ['category_name']

    def __str__(self):
        return self.category_name



class Texture(models.Model):
    code = models.CharField(max_length=50, verbose_name='کد تکسچر')
    image = models.ImageField(upload_to='texture_images/', verbose_name='تصویر تکسچر')

    class Meta:
        verbose_name = 'تصویر تکسچر'
        verbose_name_plural = 'تصاویر تکسچر ها'

    def __str__(self):
        return f"Texture {self.code}"

class Price(models.Model):
    PRICE_UNIT = [
        ('Square_meters', 'متر مربع'),
        ('roll', 'رول'),
        ('Branch', 'شاخه'),
        ('number', 'عدد'),
    ]
    UNIT_TRANSLATION = {
        'Square_meters': 'متر مربع',
        'roll': 'رول',
        'Branch': 'شاخه',
        'number': 'عدد',
    }
    unit = models.CharField(max_length=13, choices=PRICE_UNIT, default='number', verbose_name='واحد قیمت')
    price_wholesale = models.IntegerField(verbose_name='قیمت عمده')
    price_retail = models.IntegerField(verbose_name='قیمت خرده')

    class Meta:
        verbose_name = 'قیمت'
        verbose_name_plural = 'قیمت‌ها'

    def display_price(self):
        unit_str = f'واحد: {self.get_translated_unit()}' if self.unit is not None else ''
        wholesale_str = f'قیمت عمده: {self.price_wholesale}' if self.price_wholesale is not None else ''
        retail_str = f'قیمت خرده: {self.price_retail}' if self.price_retail is not None else ''

        price_str = ' | '.join(filter(None, [unit_str, wholesale_str, retail_str]))
        return price_str

    def get_translated_unit(self):
        return self.UNIT_TRANSLATION.get(self.unit, self.unit)

    def __str__(self):
        return self.display_price()

class Dimensions(models.Model):
    LENGTH_UNIT = [
        ('meter', 'متر'),
        ('millimeter', 'میلیمتر'),
        ('centimeter', 'سانتیمتر'),
        ('inch', 'اینچ'),
    ]

    WIDTH_UNIT = [
        ('meter', 'متر'),
        ('millimeter', 'میلیمتر'),
        ('centimeter', 'سانتیمتر'),
        ('inch', 'اینچ'),
    ]

    THICKNESS_UNIT = [
        ('meter', 'متر'),
        ('millimeter', 'میلیمتر'),
        ('centimeter', 'سانتیمتر'),
        ('inch', 'اینچ'),
    ]
    UNIT_TRANSLATION = {
        'meter': 'متر',
        'millimeter': 'میلیمتر',
        'centimeter': 'سانتیمتر',
        'inch': 'اینچ',
    }
    # متراژ رو اضاف کن

    length_unit = models.CharField(max_length=13, null=True, blank=True, choices=LENGTH_UNIT, default='meter', verbose_name='واحد اندازه گیری طول')
    length = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0, verbose_name='طول')

    width_unit = models.CharField(max_length=13, null=True, blank=True, choices=WIDTH_UNIT, default='meter', verbose_name='واحد اندازه گیری عرض')
    width = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0, verbose_name='عرض')

    thickness_unit = models.CharField(max_length=13, null=True, blank=True, choices=THICKNESS_UNIT, default='millimeter', verbose_name='واحد اندازه گیری ضخامت')
    thickness = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0, verbose_name='ضخامت')
    
    def get_dimensions_display(self, obj):
        if obj.dimensions:
            return obj.dimensions.display_dimensions()
        else:
            return 'No dimensions available'
        
    def get_length_display(self):
        return f'{self.length} {self.UNIT_TRANSLATION.get(self.length_unit, "")}' if self.length is not None else ''

    def get_width_display(self):
        return f'{self.width} {self.UNIT_TRANSLATION.get(self.width_unit, "")}' if self.width is not None else ''

    def get_thickness_display(self):
        return f'{self.thickness} {self.UNIT_TRANSLATION.get(self.thickness_unit, "")}' if self.thickness is not None else ''

    def display_dimensions(self):
        length_str = f"طول: {self.get_length_display()}"
        width_str = f"عرض: {self.get_width_display()}"
        thickness_str = f"ضخامت: {self.get_thickness_display()}"

        dimensions_str = ' | '.join(filter(None, [length_str, width_str, thickness_str]))
        return dimensions_str
    # update this

    
    def __str__(self):
        return self.display_dimensions()
    
    def create_from_string(cls, dimension_string):
        dimensions_list = dimension_string.split('*')
        if len(dimensions_list) == 2:
            length, width = map(int, dimensions_list)
            length, width = max(length, width), min(length, width)
            return cls.objects.create(length=length, width=width)
        else:
            return None

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='نام دسته')
    title = models.CharField(max_length=250, verbose_name='نام محصول')
    description = models.TextField(null=True, blank=True,verbose_name='توضیحات')
    price = models.ForeignKey(Price, on_delete=models.CASCADE, null=True, blank=True, related_name='products_price' ,verbose_name='قیمت')
    dimensions = models.ForeignKey(Dimensions,on_delete=models.CASCADE, null=True, blank=True, related_name='products_dimensions',verbose_name='ابعاد')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    product_code = models.CharField(max_length=3, verbose_name='کد محصول')
    images = models.ManyToManyField(Image, related_name='products', verbose_name='تصاویر')
    textures = models.ManyToManyField(Texture,blank=True, related_name='products', verbose_name='تکسچرها')
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'همه محصولات'
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['date_created']),
        ]

    def __str__(self):
        return self.title
    
    def get_selected_texture(self, texture_code):
        try:
            return self.textures.get(code=texture_code)
        except Texture.DoesNotExist:
            # Handle the case when the texture is not found
            return None


class Decoration(Product):
    class Meta:
        verbose_name = 'دکراسیون'
        verbose_name_plural = 'دکراسیون'

class Wallcoverings(Decoration):
    class Meta:
        verbose_name = 'پوشش دیواری'
        verbose_name_plural = 'پوشش‌های دیواری'


class Floorcoverings(Decoration):
    glue_10kg = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True,related_name='glue_10kg', verbose_name='چسب 10 کیلویی')
    glue_4kg = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True,related_name='glue_4kg', verbose_name='چسب 4 کیلویی')

    class Meta:
        verbose_name = 'پوشش کف'
        verbose_name_plural = 'پوشش‌های کف'


class Cornice(Decoration):
    Cornice_TRANSLATION = {
        '7': '7 سانتی',
        '9': '9 سانتی',
        'Gordeh': '(پایان کار) گرده',
        'Miane': 'میانه',
        'Tasho': 'تاشو',
        'Scouti': 'اسکوتیا',
    }
    Cornic_7 = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='cornices_7' ,verbose_name='قرنیز 7 سانتی')
    Cornic_9 = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='cornices_9' ,verbose_name='قرنیز 9 سانتی')

    Gordeh = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='Gordeh' ,verbose_name='(پایان کار) گرده')    
    Miane = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='Miane' ,verbose_name='میانه')    
    Tasho = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='Tasho' ,verbose_name='تاشو')    
    Scouti = models.ForeignKey(Price,on_delete=models.CASCADE,null=True,blank=True, related_name='Scouti' ,verbose_name='اسکوتیا')    


    class Meta:
        verbose_name = 'قرنیز'
        verbose_name_plural = 'قرنیزها'

class Curtain(Product):
    class Meta:
        verbose_name = 'پرده'
        verbose_name_plural = 'پرده‌ها'

class Readycurtain(Curtain):
    curtain_rod = models.BooleanField(default=False, verbose_name='چوب پرده')

    class Meta:
        verbose_name = 'پرده آماده'
        verbose_name_plural = 'پرده‌های آماده'

class Zebracurtain(Curtain):

    class Meta:
        verbose_name = 'پرده زبرا'
        verbose_name_plural = 'پرده‌های زبرا'
    
class Customcurtain(Curtain):
    curtain_rod = models.ForeignKey(Price,on_delete=models.CASCADE,default=False, verbose_name='چوب پرده')
    curtain_model = models.CharField(max_length=50,null=True,blank=True, verbose_name='مدل پرده')
    side_fabric = models.CharField(max_length=50,null=True,blank=True, verbose_name='پارچه کنار')
    accessory = models.ManyToManyField(Product,blank=True, related_name='Customcurtain_accessories', verbose_name='اکسسوری')

    class Meta:
        verbose_name = 'پرده سفارشی'
        verbose_name_plural = 'پرده‌های سفارشی'
        
    def get_class_name(self):
        return self.__class__.__name__

class Sofafabric(Product):
    class Meta:
        verbose_name = 'پارچه مبل'
        verbose_name_plural = 'پارچه‌های مبلی'

class Sofa(Product):
    Fabrictype = models.ForeignKey(Sofafabric, on_delete=models.CASCADE,null=True,blank=True, related_name='sofas', verbose_name='نوع پارچه')
    accessory = models.ManyToManyField(Product,blank=True ,related_name='accessories', verbose_name='اکسسوری')

    class Meta:
        verbose_name = 'مبل'
        verbose_name_plural = 'مبل‌ها'