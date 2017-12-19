## 预约实验脚本

host：http://115.156.150.131

### 登录
所需参数：

* csrfmiddlewaretoken   //uld9SyFuyAliqwohdqh7IYIMF75tkgdE
* username   //yaoqin
* password   //123456
* next  // defualt /admin/

Step:

* GET http://115.156.150.131/admin/login/?next=/admin/   // get csrftoken jzsWwq2lGjIlFXmu5HZrr4hjcIoYqR9F
* POST http://115.156.150.131/admin/login/?next=/admin/  // post csrftoken jzsWwq2lGjIlFXmu5HZrr4hjcIoYqR9F

### 提交表单

Path：/admin/reserve/reserve/add/

Content-Type:multipart/form-data; boundary=----WebKitFormBoundaryckn3Wd2rxfBUCwoG

Params: _changelist_filters=labdate__lt%3D2017-12-20%26labdate__gte%3D2017-12-18

Form Data: 

* csrfmiddlewaretoken
* Content-Disposition: form-data; name="csrfmiddlewaretoken"

O2MwtsznOPeGldXx4LSjBOMEnNwX1yaq
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="name"

姚琴
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="teacher"

吴丰顺
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="teacher_pay"

A44
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="device"

13
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="teleph"

13986272487
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="descript"


------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="regdate"

2017/12/20
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="labdate"

2017/12/25
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="labinfo"

2个Si样品
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="starttime"

15:30
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="endtime"

17:30
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="material"

Al
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="depth"

60
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="number"

1
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="temperature"

0
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="count_person"

1
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="count_taoke"

0
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="count_untaoke"

0
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="captcha_0"

bd4ec39fc14b419ed6f3e0175622860232923d40
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="captcha_1"

UUWQ
------WebKitFormBoundaryApJaHoWANgb6nnZy
Content-Disposition: form-data; name="_save"

保存
------WebKitFormBoundaryApJaHoWANgb6nnZy--
