# Compiler Design | Loop Optimazer
## Loop Jamming

Python Language

use simple source code in file to get target file

## Example
source ........
```c
int a = 0, b = 0, c = 0;

for(int i=0; i < 5; i++)
  a = i + 5;

for(int i=0; i < 10; i++)
  c = i + 5;

for(int i=0; i < 5; i++)
  b = i + 10;

cout<<a;
cout<<endl;
cout<<b;
```



## target code After Loop Jamming

```c
int a = 0, b = 0, c = 0;

for(int i=0; i < 5; i++)
{
 a = i + 5;
 b = i + 10;
}

for(int i=0; i < 10; i++)
 c = i + 5;

cout<<a;
cout<<endl;
cout<<b;
```

## by [Waad Mawlood](https://waad.netlify.app/)

lastest project [Al-Maseera Company](https://almaseera-iq.com/) | [Al-Maseera Company](https://almaseera-iq.com/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
