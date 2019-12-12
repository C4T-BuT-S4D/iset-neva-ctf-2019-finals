# Medium-100 | stego | Superdata

## Решение

> Для начала посмотрим, что выдаст нам binwalk на файл. Замечаем JPEG.
>
> Вытаскиваем картинку с помощью foremost. 
>
> В описании таска сказано, что ключ - `kek`. Пробуем `steghide extract -sf picture.jpg -p kek`. Вытаскивается flag.txt

## Флаг

`flag{w0w_y0u_4r3_sup3rc0mput3r}`
