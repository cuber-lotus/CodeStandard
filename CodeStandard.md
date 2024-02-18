# 代码规范
[toc]

# ⭐前言

## 链接

- **Github-link**: [cuber-lotus/CodeStandard: C/C++代码规范 (github.com)](https://github.com/cuber-lotus/CodeStandard) 
- **e-mail**： 1539349804@qq.com
- **QQ-Group**: 817328828
- **Bilibili**: [天赐细莲 (bilibili.com)](https://space.bilibili.com/8172252)

## 前置

本代码规范为C/C++语言(非特殊说明默认C++11~)。

其他语言学习者也可以互相借鉴。

## 目的

制定一份通俗易懂的编码规范。

规范团队代码，提升代码阅读效率。

## 宗旨

- 代码是死的，人是活的。
- 坚持一个能跑原则。
- 优先保证代码和程序的正确性。

## 使用说明

本规范可以直接二次修改供中小公司或团队使用。

本文的规范无需完全遵守，若有更合理规范可自行进行二次修改。



# ⭐包和文件

## 用路径来管理不同模块

不同模块应该用不同的包来进行管理。

三方包(库)应该放在单独的包中。

```bash
demo:
├─3rdparty
├─controller
├─entity
├─utils
└─server
```

## 头文件与源文件

**核心职责**

- **头文件**: 负责声明
- **原文件**: 负责实现

**命名**

头文件和源文件应该保持同名或强关联的名称（如：具有相关前缀）

**后缀名**

| 头文件         | 源文件                    |
| -------------- | ------------------------- |
| .h; .hpp; .hxx | .c; .cpp; .cc; .cxx; .tcc |

**分包**

由于头文件和源文件的职责不同，应该分包。

有的ide会自动识别分包。

| 头文件                           | 源文件                        |
| -------------------------------- | ----------------------------- |
| public<br />include<br />headers | private<br />src<br />sources |

**扇入扇出**

使用[Pimpl](https://github.com/isocpp/CppCoreGuidelines/blob/master/CppCoreGuidelines.md#Ri-pimpl)的技巧减少头文件中include的扇入。

**字符集**

头文件和源文件的字符集应该保持一致。

## 文件

- 整个项目的应该保持统一的字符集
- 用空格代替`tab` (一般推荐2或4或8空格)



# ⭐注释

**注释是为了用人话表达代码的含义。**

注释必须有意义。不要废话文学。

## /**/与//

|              | `/**/`                   | `//`                 |
| ------------ | ------------------------ | -------------------- |
| **内容数量** | 行数较多                 | 行数较少             |
| **举例**     | 文件头注释<br />函数注释 | 函数内某条语句的解释 |

## 文件头注释

可以借助现代ide来帮助生成头文件注释的模板。

- **头文件**中应该解释本文件的使用说明。

- **源文件**中应该简单描述本文件的编写思路。

下面将列举文件头注释的常用标注类型。

| Name      | Expression |
| --------- | ---------- |
| Copyright | 版权说明   |
| @file     | 文件名     |
| @author   | 作者       |
| @date     | 日期       |
| @version  | 版本号     |
| @Email    | 邮箱       |
| @brief    | 描述       |

```cpp
/***************************************************************************
 * Copyright © 202x
 * All right reserved. See COPYRIGHT for detailed Information.
 * @file       main.cpp
 * @author     cuber-lotus
 * @Email      1539349804@qq.com
 * @date       202x-xx-xx
 * @version    1.0.0
 * @brief	   
 * 文件描述一般会有多行
 * 每行不要超出首行和底行的长度
 ***************************************************************************/
```

## 类注释

若目标类就是文件中的唯一类，则文件注释就应该表示当前类的作用。

若一个文件存在多个类，或者存在内部类，则应该把每个类或封装体都做注释解释。

若存在**友元**则必须对友元的关系进行说明。

```cpp
/**
 * @brief The Base class
 * This is a class for example
 */
class Base {
public:
    Base();
};
```

## 函数注释

- 标注所有入参和出参
- 若入参包含默认值，也应该加以说明
- 若入参为引用，也应该加以说明
- 若为友元则需说明

```cpp
/**
 * @brief add
 * @param a &
 * @param b default = 0
 * @return 
 * The function of this function is used to obtain the sum of two numbers
 */
int add(int &a, int b = 0) {
    return a + b;
}
```

## 代码注释

- 置于代码块直接上方
- 与代码块缩进一致

**注释应置于代码的直接上方**

```cpp
// good
/**
 * @brief fun
 */
void fun() {
}

// bad 缩进不一致
    /**
     * @brief fun
     */
void fun() {
}

// bad 非直接上方
void fun() { // @brief fun
}
```

## TODO注释

TODO注释通常表示当前的代码是一种临时或者不完全的代码。

需要标注编写者，联系方式，编写时间等信息。

另外推荐使用与上下文风格不同的注释标注。（不固定）

核心目的是为了醒目！

```cpp
int fun (int x) {
    /** !!!!!!!!!!!!!!!!!!!!!!!!
     !!! TODO(cuber-lotus)
     !!! TODO(1539349804@qq.com)
     !!! TODO(2023年2月29日)
     !!! 这是一份临时方案，因为。。。
     !!!!!!!!!!!!!!!!!!!!!!!! */
    return x + 114514;
}
```

## 尾部注释

部分情况需要进行尾部的注释：

- namespace
- #endif
- 较大范围，嵌套层数较多的括号

```cpp
#ifndef FILE_HPP
#define FILE_HPP

namespace NAME {

void fun() {
    ::std::vector<int> arr;
    while (1) {
        for (int i = 0; i < arr.size(); i += 1) {
            if (0 == arr[i]) {
                ::std::sort(arr.begin(), arr.begin() + i,
                            [](int a, int b) {
                                return a < b; 
                            });
            }
        }
    }  // while (1)
}

}  // namespace NAME

#endif // FILE_HPP
```

## 细节技巧

- `//` 后空一格
- 注释内容为重要单词或变量时可加引号或者前后空格，便于直接双击选取
  - `// 这是这个 class 的注释`
  - `// 这是这个'class'的注释`
- `/**/` 中间的每行可以加`*`或其他来美化代码

## 特殊情况

在具有并列含义，如枚举变量时，直接在右侧写注释既清晰又美观。

```cpp
/**
 * @brief The ColorEnum enum
 */
enum ColorEnum {
    COLOR_RED,  // 红色
    COLOR_BLUE  // 蓝色
};
```



# ⭐缩进

## 使用空格而不是tab

禁止tab缩进，使用空格缩进4字符。(可2字符或8字符，遵循项目统一)

## 注释与注释目标对齐

注释相关内容具体见注释标准。

## 类权限与class关键字对齐

```cpp
// 全局类
class A {
public:
    // 嵌套类
    struct B {
    public:
    protected:
    private:
    };

protected:
private:
};
```

## 不缩进情况

- 文件头注释
- 预处理机制 `#`
- namespace
- goto 跳转目标

```cpp
/**
 * @copyright Copyright (c) 2023
 */

#define FILE_NAME_HPP

namespace NAME1 {
namespace NAME2 {

/**
 * @brief 
 * 
 * @param arr 
 * @param len 
 * @return int* 
 */
int* find_0(int arr[], int len) {
    int* idx = nullptr;
    for (int i = 0; i < len; i += 1) {
        if (0 == *(arr + i)) {
            idx = arr + i;
            goto finded;
        }
    }

finded:
    return idx;
}

}  // namespace NAME2
}  // namespace NAME1
```

## 行长的限定

不得超出屏幕可视范围的80%，由于每个人的屏幕等因素不一样，一般规定为80~120字符。

> 因为历史遗留原因，部分规范规定一直规定是80字符，但随着发展可适当增加长度。

## 换行

当一行内容太长时，应该换行。

至少有一组缩进（与上一行），若有并列意义的内容可与该内容对齐。

```cpp
#include <bits/stdc++.h>

int main() {
    int arr[5];

    // good
    // while的判断太长
    // 一组空格
    do {
        // todo
    } while (arr[0] == arr[1] && arr[1] == arr[2] && arr[2] == arr[3] &&
        arr[3] == arr[4] && arr[4] == arr[5]);

    // good
    // while的判断太长
    // 与并列的内容对齐
    do {
        // todo
    } while (arr[0] == arr[1] && arr[1] == arr[2] && arr[2] == arr[3] &&
             arr[3] == arr[4] && arr[4] == arr[5]);

    return 0;
}
```

## 空行

具有相对独立或者完整的功能块之间应换行，空行。

```cpp
#include <bits/stdc++.h>

// [1]
// 预处理指令与函数间的空行
void fun(int (&arr)[5]) {
}

// [2]
// 函数间空行
int main() {
    // [2.1]
    // 声明并初始化
    int arr[5];
    memset(arr, 0x3f, sizeof(arr));
	
    // [2.2]
    // 具体操作
    fun(arr);
	
    // [2.3]
    // 其他操作(与上一操作是否有强关联而定)
    for (int x : arr) {
    }
	
    // [2.4]
    // return
    return 0;
}
```


# ⭐语句块

本文默认左大括号不换行。在部分C语言规范中要求左括号换行。

> 在Golang语言中，将左括号是否换行定为了语法规范

保持同一函数和同一文件的一致性。

## 勿一行声明多个变量

一行应该仅声明一个变量

- 便于表达独立的语义
- 便于cv限定符，*[]，&等符号的作用限定

EXC：若具有强关联的并列属性可以同行。

```cpp
struct Cube {
    int l, w, h;
    int volume;
    int surface;
};
```

## for, while, if, switch, case, do, goto, try

- 有`()`的前后都加空格
- 有`:`的后侧加空格
- 必须加`{}`构成块级作用域

## if else

> try catch 同理

分支较短的else可以跟在}后面

分支较多的需要换行便于加注释描述

```cpp
#include <string>

enum SEX {
    SEX_Male,        // male
    SEX_Female,      // female
    SEX_Intersex,    // intersex
    SEX_Androgynous  // androgynous
};

::std::string Ask_sex(const SEX type) {
    if (type == SEX_Male) {
        return "Male";
    } else {
        return "Female";
    }
}

::std::string Ask_sexDetail(const SEX type) {
    // 默认 false 为了保持下面整齐
    if (false) {
    }
    // male 男性
    else if (type == SEX_Male) {
        return "Male";
    }
    // female 女性
    else if (type == SEX_Female) {
        return "Female";
    }
    // intersex 双性人
    else if (type == SEX_Intersex) {
        return "Intersex";
    }
    // androgynous 不男不女
    else if (type == SEX_Androgynous) {
        return "Androgynous";
    }
    // default
    else {
        return "Sex Error";
    }
}
```

## switch

注意，switch-case的原理与goto类似，是立即跳转的。

- 每个case必须包含`{}`构成块级作用域
- 必须有默认default
- break在大括号外
- 不得在非`{}`中声明变量
- case是否缩进均可

```cpp
#include <string>

enum SEX {
    SEX_Male,    // male
    SEX_Female,  // female
};

::std::string Ask_sexDetail(const SEX type) {
    switch (type) {
    // male 男性
    case SEX_Male: {
        return "Male";
    } break;
    // female 女性
    case SEX_Female: {
        return "Female";
    } break;
    // default
    default: {
        return "Sex Error";
    } break;
    }
}
```

## goto

时常听到有些地方提倡禁止使用goto。

但是本文要求的是，可以使用goto，但是在**任何用到goto的地方必须加以大量的注释和说明！**且保证goto不会出现跳过声明，跨编译器编译错误等诸多问题！

推荐在跳转标签后加`;`以便一些语法解析操作。

## 逗号后加空格

如果逗号后没有内容，或者是域的结束就没必要加空格了。

## 判断语句较长时运算符换行保持统一

```cpp
int main() {
    int arr[5];
    
    // 两种写法均可
    // good
    if (arr[0] == arr[1] && arr[1] == arr[2] && 
        arr[2] == arr[3] && arr[3] == arr[4] && 
        arr[4] == arr[5]) {
    }
    
    // good
    if (arr[0] == arr[1] && arr[1] == arr[2] 
        && arr[2] == arr[3] && arr[3] == arr[4] 
        && arr[4] == arr[5]) {
    }
    
    // bad
    if (arr[0] == arr[1] && arr[1] == arr[2] &&
        arr[2] == arr[3] && arr[3] == arr[4] 
        && arr[4] == arr[5]) {
    }
   
    return 0;
}
```

## 指针和引用左右选择一边留空格

&推荐贴近变量名的一侧。

```cpp
// good
void funGood(int *p, int &ref) {
}

// bad
void funBad(int * p, int&ref) {
}
```

## 综合举例

```cpp
#define M 100

int main() {
    int arr[M];
	
    auto check = [](int arr[], int len) {
        bool flag = (nullptr == arr);
        switch (len & 1) {
        case 0: {
            flag &= false;
        } break;
        default: {
            flag &= true;
        } break;
        }
        return flag;
    };

    int cnt = 0;
    for (int i = 0; i < M; i += 1) {
        if (true == check(arr, i)) {
            cnt += 1;
        }
    }

    return 0;
}
```



# ⭐命名

命名规范是代码和项目规范中最重要的内容之一，也是离每个程序员最贴近的规范。

**注意：**

- **命名规范应该根据团队自身的决议**
- 不要看到在网上别人或者源码怎么写就去模仿
- 不要和编译器，框架，三方库等等命名方式冲突
- 注意包和文件命名的大小写在不同平台的区别（win, linux, ios）
- 千万不要和**宏冲突**，宏一般为全大写

> 下方列出多个方案仅供参考，团队选取一种遵循即可

## 常用命名规范类型

| 方式           | 举例         |
| -------------- | ------------ |
| 小驼峰         | `redApple`   |
| 大驼峰         | `RedApple`   |
| 下划线         | `red_apple`  |
| 匈牙利命名法则 | `m_redApple` |

## 长度应该适中

|      | 过短                                   | 过长                                              |
| ---- | -------------------------------------- | ------------------------------------------------- |
| 举例 | `int a;`                               | `void Refresh_bigRoundRedWoodenChineseTable() {}` |
| 坏处 | 过短的命名一般来说就是名称的含义不明确 | 过长一般是因为耦合了太多内容，这是一种解耦的提示  |

## 缩写

命名应该清晰的表达出含义，因此不推荐使用各种缩写。

允许的缩写：

- 约定俗成
- 与项目业务相关

**约定俗成的缩写**

太多了，这里仅列举几个。

| 原单词   | 缩写  |
| -------- | ----- |
| 循环变量 | i,j,k |
| temp     | tmp   |
| value    | val   |
| object   | obj   |

## 文件

> 启动文件名为`main`。
>
> 启动函数为`main`请勿随意修改。

以类文件为例：

注意点：

- 禁止出现短横线`-`
- 源文件名 != object文件名 （尽量避免大写）
  - Windows 不区分大小写
  - Linux 区分大小写

| 格式 `<路径>_<类名>` | 举例                       |
| -------------------- | -------------------------- |
| 路径小写，类名大驼峰 | `widget_set_DeviceMessage` |
| 路径小写，类名全小写 | `widget_set_devicemessage` |

**防重包含宏**

| 格式                                | 举例                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| 全大写+下划线+文件名后缀+**时间戳** | `WIDGET_SET_DEVICEMESSAGE_H_1679896661`<br />`WIDGET_SET_DEVICEMESSAGE_HPP_1679896661` |
| 乱码（只要你敢）                    | `fgGG5gs___$$25aeL36g$SDGfsA5`                               |

## namespace

> 静止在大范围内直接 `using namespace`

| 格式       | 举例                 |
| ---------- | -------------------- |
| 全小写     | namespace my_name {} |
| 首字母大写 | namespace My_Name {} |

## class & struct

大驼峰

## 函数

| 格式 （动词_具体作用作用） | 举例           | 备注           | 举例                       |
| -------------------------- | -------------- | -------------- | -------------------------- |
| 小写动词_小驼峰            | get_redApple() | 仅内部辅助作用 | private<br />匿名namespace |
| 大写动词_小驼峰            | Get_redApple() | 外部可调用     | public<br />全局           |

## 变量

在一些特殊情况允许使用`_`或`$`，请自行斟酌！

| 场景                    | 举例                       | 备注                                                        |
| ----------------------- | -------------------------- | ----------------------------------------------------------- |
| 全局                    | g_redApple                 |                                                             |
| 成员变量                | m_redApple<br />redApple_  | 请加特殊表示如`前m_`或`后缀_`便于使用时与参数和临时变量冲突 |
| 静态变量                | s_redApple                 |                                                             |
| 常量                    | k_redApple<br />c_redApple | 常量可采用大驼峰形式，枚举同理                              |
| 函数内普通变量/函数参数 | redApple                   | 注意名称覆盖问题                                            |

## 宏

注意，别于内置和框架宏冲突，造成多次展开等问题。

| 格式          | 举例                             |
| ------------- | -------------------------------- |
| 全大写+下划线 | MIN(x, y)<br />CHECK_RANGE(x, y) |

## enum

| 格式                   | 举例      |
| ---------------------- | --------- |
| **枚举名** 大驼峰      | ColorEnum |
| **枚举量** 前缀+大驼峰 | Color_Red |

枚举天然的具有并列的特点，因此推荐在再每个枚举量前加上整个枚举类型的特性。

这既可以避免枚举的重名，又可以让程序员充分利用ide的代码提示。

```cpp
enum ColorEnum {
    COLOR_Red,  // 红色
    COLOR_Blue  // 蓝色
};
```

## union

- 联合体名 -> 大驼峰
- 成员 -> 小驼峰

## using和typedef

- C语言中使用typedef
- C++中使用using（请不要再用typedef）

注意，这两者都是有作用范围的。

## 用相同类别的属性作为前缀表示

这里指的**属性**非常宽泛，见下方举例体会。

- 便于使用编辑器的时候输入首字母直接给出批量提示
- 便于明确变量类型

```cpp
// 此处以下下划线表示法为例
Button *btn_close;
Button *btn_open;

String user_name;
String user_password; 

Event *event_show;
Event *event_hide;
```

## 特殊字符说明

勿使用`$`，在部分框架中该字符设计一些重链接性问题。

勿使用`_`开头，因为该命名方式一般用于底层库的使用和编译器的解析，因为为了防止冲突请不要以下划线开头。

## 注意

namespace和类都有域的概念，两者的命名风格推荐应该不一致

```cpp
// 解释1 namespace scope_a 中有 class scope_b 定义一个对象x
// 解释2 class scope_a 中有内部类 class scope_b 定义一个对象x
scope_a::scope_b x;
```



# ⭐运算符

> 注意：请勿滥用运算符重载

## 多元运算符要左右空格

一般为算数，赋值等运算符

```cpp
// good
const int M = 1e9 + 7;
int arr[M] = {};
for (int i = 0; i < M; i += 1) {
    arr[i] = i & 1 ? i + M : i * M;
}

// bad
const int M=1e9+7;
int arr[M]={};
for (int i=0; i<M; i+=1) {
    arr[i]=i&1?i+M:i*M;
}
```

## 一元运算符要贴近变量

```cpp
// good
void fun(int *x, int &y) {
    *x = -1;
    y = ~*x;

    ++*x;
    y = !y;
}

// bad
void fun(int * x, int & y) {
    * x = - 1;
    y = ~ * x;

    ++ * x;
    y = ! y;
}
```

## 成员访问符号要贴近变量

一元或二元访问符都要求贴近变量

> 注意：在C++17前不保证左右的运算顺序

```cpp
// 一元
*a
&a
// 二元
a[b]
a.b
a->b
a.*b
a->*b
```

## 减少使用自增++和自减--

> 自增自减在一些语言中已经不支持，如：Python

**危害：**

- 自增，自减在混合运算中，在不同编译器中实现的效果是不一样的
- 使用宏定义时，可能会执行多次

| 自增/自减     | 替代                 |
| ------------- | -------------------- |
| `i++; / ++i;` | `i += 1;`            |
| `i--; / --i;` | `i += -1; / i -= 1;` |

## 使用括号增加可读性

在一些位运算，较长的逻辑判断时，应该增加括号来增加可读性和准确性。

实在过长则应该跨行来编写。

```cpp
// good
if ((a && (b + 1)) || ((c << d) | e)) {
}

// bad
if (a && b + 1 || c << d | e) {
}
```

## 比较运算符左侧尽量写常量

部分现代编译器和ide会有单等号的提示。且从左往右读更符合人的思考和阅读习惯。

因此如何能保证正确，则该条说明不强制，单前提是保证了正确。

```cpp
void* p;
int x;

// good
if (NULL == p) {
}
if (0 == x) {
}

// bad
// == 容易写成 =
if (p == NULL) {
}
if (x == 0) {
}
```

## 显示的布尔判断代替非0即1

**非0即1的危害：**

- 无法明示类型
- 会出现隐式类型转换

```cpp
// good
// 明示flag是一个布尔运算符 （虽然不绝对是）
if (true == flag) {
}

// bad
// 不明确类型
if (flag) {
}
```

## 运算符重载

- 时刻注意运算符重载的本质是函数的调用。
- 禁止滥用运算符重载
- 赋值运算符应与拷贝，移动构造的效果保持一致
- 慎用类型转换
- 禁止重载&&||,等运算符
- **TODO**



# ⭐函数

## 函数功能应该明确

每个函数应该有自己专属的功能，不要一个函数处理多个任务。

参数个数不易过多，除非是一系列并列性质的参数。

**不明确的信号**：

- 超过100行
- 入参过多
- 做过多判断
- 扇出高于10

## 使用引用，减少使用指针

在C++中引用的提出极大的提升了函数传参的便捷性。

指针有空指针和野指针的情况，而引用有明确对象。（虽说也有空引用的隐性危险）

```cpp
// C语言式传参
void c_swap(int *a, int *b) {
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

// C++式传参
void cpp_swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}
```

## 用const表示允许修改与否

```cpp
#include <string>

// 不许修改
void show(const std::string& str) {
}

// 允许或希望修改
void modify(std::string& str) {
}

// 希望所有权转移
void modify(std::string&& str) {
}
```

## 右值引用使用std::move转发引用使用std::forward

```CPP
#include <string>
#include <utility>

void fun(std::string&& str) {
    std::move(str);
}

template <typename Type>
void fun(Type&& arg) {
    std::forward<Type>(arg);
}
```

## 重载函数应该相邻编写

```cpp
// good
void swap(int &a, int &b) {
}
void swap(double &a, double &b) {
}
void fun() {
}

// bad
void swap(int &a, int &b) {
}
void fun() {
}
void swap(double &a, double &b) {
}
```

## 指针参数应该检测合法性

```cpp
void fun(void* p) {
    if (nullptr == p) {
        // pass
    } else {
        // pass
    }
}
```

## lambda表达式

> 注意：lambda表达式的本质是一个具有仿函数的匿名类的**匿名对象**，属于可调用对象
>
> 不知道本质的话，很多情况就会搞不清了

**适用场景**：

- 某个函数仅作单词或少量调用
- 算法函数的谓词或回调
- 想要用到大量当前函数的局部变量时
- 不想污染全局空间
- 调用次数较少，具有特化性质

## 返回值应该明确类型

无论是入参还是出参，都应该给外部明确。

在C++11中提出了尾值返回，在C++14中支持返回值写成`decltype(auto)`。

在外部接收时，不要理所当然的以为是自己知道的类型，然后就使用auto。

```cpp
#include <vector>
// C++14
// 下面是返回值`加()`和`不加()`的区别举例
struct Node {
    int x;
    // 返回值不带() int
    auto fun0() -> decltype(auto) {
        return x;
    }
    // 返回值带()   int&
    auto fun1() -> decltype(auto) {
        return (x);
    }
};

int main() {
    Node node;
    // T0 右值引用
    // T1 左值引用
    auto &&x0 = node.fun0();
    auto &&x1 = node.fun1();
    using T0 = decltype(x0);
    using T1 = decltype(x1);

    ::std::vector<bool> arr(10);
    // 明确返回值类型
    bool b0 = arr[0];
    // ::std::vector<bool> 是一个特化版本
    // operator[]的返回值是 class _Bit_reference in gnu-gcc
    auto b1 = arr[0];

    return 0;
}
```

## 禁止悬空返回

出现悬空的核心就是在于没有理清对象的生存周期。

**常见悬空返回**：

- 栈空间释放
- 临时的右值释放

```cpp
int* fun0() {
    int x;
    return &x;
}

int& fun1() {
    int x;
    return x;
}

auto fun2() {
    int x;
    return [&] {};
}

int main() {
    // dangling pointer
    int* p = fun0();
    // dangling reference
    int& ref = fun1();
    // lambda dangling reference
    auto lam = fun2();
    
    return 0;
}
```



# ⭐类

> class和struct的**唯一**区别就是默认权限不同

## 继承顺序

C++允许多继承和不同权限的继承

但是一般来说多继承会出现很多意想不到的问题，因此不推荐多继承，绝大多数情况请直接使用public继承。

但有一种情况推荐多继承，就是一个主的继承类，其他都是抽象类用于统一接口。

1. 主继承类
2. 抽象类

> tips: 多继承在一些其他语言中废弃，如java

## 权限顺序

1. public
2. protected
3. private

## 内容顺序

**类型顺序**：

1. 友元
   1. 友元类
   2. 友元函数
2. using 声明
3. 封装体
   1. enum
   2. union
   3. class & struct
4. 静态变量
5. 静态函数
6. 成员变量
7. 构造函数
8. 析构函数
9. 成员函数
10. 运算符重载

**变量顺序**：

- 常量
- 引用
- 普通对象

## 构造函数顺序

- 无参
- 拷贝
- 移动
- 有参

```cpp
class MyClass {
public:
    MyClass();
    MyClass(const MyClass&);
    MyClass(MyClass&&);
    MyClass(int x);

    ~MyClass();
    
    // void fun();
};
```

## 运算符重载顺序

> [C++ 运算符优先级 - cppreference.com](https://zh.cppreference.com/w/cpp/language/operator_precedence)

遵循运算符默认顺序。

由于一般没人会把运算符优先级全记住，因此只要求将同类运算符重载定义在一块即可。

请勿与全局运算符重载重定义产生二义性。

## 使用explicit避免隐式类型转换

```cpp
class MyClass {
public:
    explicit MyClass(int x, int y = 10) {
    }
};
```

## 自定义拷贝和移动语义

当设计较复杂结构，或者有内存管理的时候，应该自定义拷贝和移动语义。

拷贝构造，拷贝赋值; 移动构造，移动赋值。**要求成对出现或禁止**。

## 使用override, delete, default, final

使用C++11提出的这些关键词明示作用。

注意，显示删除的函数也参与重载决议。

## 特殊情况

实际编码中，受到业务和设计模式的影响，不必严格遵循上述要求。

```cpp
/**
 * @brief
 * 上文提到函数应该遵守先public再private的原则
 * 但这里强制要求外部调用一个有参构造
 * 但可以通过委托构造的方式，先初始化一些其他内容
 * 减少有参构造出现过度冗余代码
 * 而此处无参构造的调用时优先于有参的，写在上面更加清晰
 */
class MyClass {
private:
    int x;
    int y;

private:
    // 无参构造函数
    MyClass() : x(0), y(0) {
    }

public:
    // 有参委托构造函数
    MyClass(int y) : MyClass() {
        this->y = y;
    }
};
```



# ⭐内存管理

> 💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥
>
> 💥强烈推荐：[Memory-Manage-Together](https://github.com/cuber-lotus/Memory-Manage-Together) 💥
>
> 💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥
>
> **“C makes it easy to shoot yourself in the foot; C++ makes it harder, but when you do it blows your whole leg off”**
>
> **--- Bjarne Stroustrup's FAQ**

**核心思想：知道对象在整个程序中的生存周期。**

即使具有再多技巧，如果不能理解对象的生命周期，全是白搭。

## 使用new/delete而非malloc/free

**new/delete的优势：**

- new/delete 会调用构造和析构
- new/delete 能让程序员偏向于对象的思维
- new/delete 支持对基本类型的操作

关于new和delete的重载，参见运算符重载章节

## 合理使用智能指针

C++运用RAII机制定义了内置的标准智能指针，来帮助编程人员自动管理内存。

但是并不是所有情况都应该用智能指针。很多在使用智能指针的场景，可以用`对象+引用`的方式代替。

注意`::std::unique_ptr和::std::share_ptr`的使用区别和使用细节。

> 注意：智能指针的线程不安全的

**不适用智能指针的场景**：

一个核心：人家有自己的生存周期，你别管。

- 全局的变量/全局公用内存
- 单例模式
- 类的静态成员
- 外部具有自己生存周期的内存



# ⭐其他

## 宏

宏并非一无是处，但是**能不用就不要用**。

| 作用   | 替代                            |
| ------ | ------------------------------- |
| 数值   | 常量, constexpr                 |
| 字符串 | const string，const char* const |
| 函数   | 模板函数，内联函数              |

## 异常

**TODO**

注意异常传参和函数传参的区别。

## 类型转换

使用casting，而非传统C语言的强转。

## 明示类型长度

不同编译器和硬件平台对同一关键词类型的实现可能不同，且32位和64位系统也会有差异。

例如：long在标准中规定为 `int <= long <= long long` 。

主要针对该变量是有位数有要求的情况。

```cpp
// 此文件下定义了常用的长度表示
#include <stdint.h>
//! 注意，不同平台和编译器有差异
//! 此处展示为 gcc version 7.3.0 (i686-posix-dwarf-rev0, Built by MinGW-W64 project)
typedef signed char        int8_t;
typedef unsigned char      uint8_t;
typedef short              int16_t;
typedef unsigned short     uint16_t;
typedef int                int32_t;
typedef unsigned           uint32_t;
typedef long long          int64_t;
typedef unsigned long long uint64_t;
```

## 初始化

初始化是一门非常大的学问，当你用任意一种初始化方式时，请确保你自己非常了解这种初始化方式。

- 变量使用前要求初始化
- 推荐使用大括号初始化
  - 但是=和()这两种方式已经深入人心了，因此继续用也没问题。
  - 注意三种初始化的区别 （不同点非常多，看个人积累）

```cpp
#include <string>
#include <vector>

// 注意这几种初始化方式的不同细节
int main() {
    // 这是函数声明
    // 两个的参数又不一样
    ::std::string test0(::std::string());
    ::std::string test1(::std::string = "");
    // 这是变量定义
    ::std::string test2(::std::string{});

    // [4, 4, 4]
    ::std::vector<int> arr0(3, 4);
    // [3, 4]
    ::std::vector<int> arr2{3, 4};

    // int
    auto num0 = 1;
    // int
    auto num1(1);
    
    // {} in msvc C++17
    // int
    auto num3{1};
    // class std::initializer_list<int>
    auto num4 = {1};

    return 0;
}
```



# ⭐团队合作

## 不要修改不是自己写的文件

## 不要修改已经确定提供给外部的接口名

## include 相对路径

## 修改TODO操作需与编写者或负责人协商

## 重构的code一定要重新测试

## 不要为了装逼用让同事看不懂的技巧

## 截图要全

- 使用截屏软件，防止伤害别人的眼睛
- 必须连行号一起截取
- 行尾要全
  - 代码行
  - 注释行
- 报错信息要全

## 对团队成员保持宽容

没有人有义务帮助你改bug

每个人的时间都很宝贵



# ⭐后记

> **e-mail**: 1539349804@qq.com
>
> [天赐细莲-哔哩哔哩](https://space.bilibili.com/8172252)
>
> 有相关建议可以直接提交issue
>
> 非常非常非常欢迎讨论交流补充，或者团队想要二次加工建议等


---
---
---
# END
