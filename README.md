Закончил с проектом, мне кажется, выполнил все пункты. Немного распишу, что сделал за месяц.
1. Создал модель User с теми же полями, что и в дефолтной модели, решил указать всё, что есть, чтобы разобраться как можно лучше,
   добавил поле type с двумя вариантами(male и female). Только не указал методы(тут вопросы есть)
   Чтобы вид был более презентабельный, я оформил его немного. Всё же приятнее так.
2. Создал свою модель Group, связал её с моделью User. Но, мне кажется, что тут что-то не так, потому что права не применяются(
   Чтобы мои модели работали я их указал в settings.py
3. Помимо этого, также создал две модели(Crypto и Category), связал их между собой и с моделью User(OneToMany)
4. Реализовал в приложении регистрацию и вход пользователя, как на самом сайте, так и в панели администратора,
   также там(панель администратора) можно изменять пароль пользователя, на самом сайте тоже. Реализовал алгоритм смены пароля через почту после того, как пользователь забыл пароль
5. При желании, каждый пользователь может сменить пароль, после входа на свою страницу
6. Улучшил панель администратора
   ---ТРУДНОСТИ--
   1. Не могу пока что разобраться, как публиковать проект с БД

Буду ждать критику. С уважением АВ
