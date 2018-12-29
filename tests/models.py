from trod import Trod
from trod.types import field, index


db = Trod()


class TestTypesModel(db.Model):
    __table__ = 'test_types_table'
    __comment__ = '测试用例'
    __auto_pk__ = True

    tinyint = field.Tinyint(1, unsigned=True, allow_null=False, default=0, comment='tinyint test')
    smallint = field.Smallint(10, default=0, comment='smallint test')
    int_ = field.Int(30, unsigned=True, allow_null=False, default=0, comment='int test')
    bigint = field.Bigint(30, unsigned=True, allow_null=False, default=0, comment='bigint test')
    text = field.Text(encoding='utf8mb4', allow_null=False, comment='text test')
    string = field.String(45, use_varchar=True, allow_null=False, default='', comment='string test')
    float_ = field.Float((3, 3), default=0, comment='float test').modify()
    double_ = field.Double((4, 4), unsigned=True, default=0, comment='double test')
    decimal = field.Decimal((4, 4), unsigned=True, default=0, comment='decimal test')
    now = field.Datetime(comment='datetime test')
    now_too = field.Timestamp(comment='now ts')
    created_at = field.Timestamp(auto='on_create', comment='created_at')
    updated_at = field.Timestamp(auto='on_update', comment='updated_at')

    key = index.Key(column=['tinyint', 'now'], comment='key test')
    unique_key = index.UniqueKey(column='string', comment='unique key test')


class User(db.Model):
    __table__ = 'user'
    __comment__ = '测试用例'

    id = field.Bigint(45, unsigned=True, allow_null=False, primary_key=True, comment='主键')
    name = field.String(45, use_varchar=True, allow_null=False, comment='用户名')
    num = field.Bigint(45, unsigned=True, default=0, comment='唯一号码')
    password = field.String(45, use_varchar=True, comment='密码')
    sex = field.Tinyint(1, unsigned=True, allow_null=False, default=0, comment='性别')
    age = field.Smallint(3, unsigned=True, default=0, comment='年龄')
    date = field.Datetime(comment='注册时间')
    created_at = field.Timestamp(auto='on_create', comment='created_at')
    updated_at = field.Timestamp(auto='on_update', comment='updated_at')

    name_idx = index.Key(column='name')
    num_unidx = index.UniqueKey(column='num')