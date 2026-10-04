---
ru: "2026/2027 Анализ и прогнозирование временных рядов методами искусственного интеллекта (очная)"
en: "Analysis and Forecasting of Time Series using Artificial Intelligence Methods"
code: "AFTSAIM-2026"
origin: "https://edu.susu.ru/course/view.php?id=216939"
---

<!--
Правила заполнения COURSE.md

Метаданные: оставьте ровно четыре строковых поля в YAML frontmatter.
- ru: русское название курса из Moodle.
- en: английский перевод названия курса.
- code: согласованное имя репозитория <EnglishAcronym>-<YYYY>; только английские буквы, цифры и дефисы, без префиксов программы и формы обучения.
- origin: каноническая ссылка страницы курса Moodle с идентификатором курса, без сессионных параметров.
Замените заполнители подтвержденными данными; сохраняйте уже согласованные значения.

Замените заголовок названием из источника, а заполнитель ниже — учебным содержанием страницы курса.
Перенесите описание, преподавателей, правила оценки и все разделы с названиями элементов и ссылками в исходном порядке.
Преобразуйте HTML в Markdown, сохраняя язык, формулировки, абзацы, списки, выделение, формулы и ссылки. Не пересказывайте и не исправляйте исходный текст.
Не добавляйте разделы или сведения, которых нет в источнике.
Исключите интерфейс Moodle, личные оценки, ответы, комментарии, обратную связь и статусы выполнения. Не сохраняйте cookies, токены и сессионные данные.
Если источник недоступен, сохраните существующую выгрузку и сообщите об ограничении; не придумывайте недостающие сведения.
-->

# 2026/2027 Анализ и прогнозирование временных рядов методами искусственного интеллекта (очная)

## Сведения о дисциплине

##### **Преподаватели**

- *Лектор:* [Михаил Леонидович Цымблер](https://mzym.susu.ru/), д.ф.-м.н., профессор [кафедры системного программирования](https://sp.susu.ru/) ([mzym@susu.ru](mailto:mzym@susu.ru))
- *Ассистент:* Андрей Игоревич Гоглачев, ст. преподаватель [кафедры системного программирования](https://sp.susu.ru/) ([goglachevai@susu.ru](mailto:goglachevai@susu.ru))

##### **Структура курса**

- *Лекции:* 16 час.
- *Практики:* 32 час
- *Форма контроля:* экзамен

##### **Краткое описание курса**

*Целью курса* является ознакомление студентов с основными методами и алгоритмами решения задач интеллектуального анализа временных рядов. *Результатом обучения* являются умение и навыки применения указанных методов и алгоритмов при решении практических задач из реальных предметных областей.
Курс покрывает следующие *основные темы*:

- *Введение в дисциплину.* Основные понятия: временной ряд, подпоследовательность. Основные задачи интеллектуального анализа временных рядов: поиск аномалий, поиск мотивов, поиск по образцу, восстановление пропусков, прогноз.
- *Поиск подпоследовательностей по образцу*. Мера динамической трансформации времени (DTW, Dynamic Time Warping). Поиск на основе техники нижних границ.
- *Поиск аномалий во временных рядах.* Понятие диссонанса. Алгоритм HotSAX. Понятие диапазонного диссонанса. Алгоритмы DRAG и MERLIN.
- *Матричный профиль временного ряда*. Понятие матричного профиля. Применение матричного профиля для решения задач интеллектуального анализа временных рядов. Алгоритмы вычисления матричного профиля.
- *Аналитические примитивы на основе матричного профиля*. Поиск сниппетов (типичных подпоследовательностей). Поиск цепочек (эволюционирующих шаблонов).
- *Восстановление и прогноз временного ряда*. Аналитические алгоритмы восстановления временного ряда. Восстановление ряда с помощью нейронных сетей. Прогнозирование временных рядов с помощью модели ARIMA.

##### **Литература**

- *Основная*
  - Aggarwal C.C. Data Mining: The Textbook. Springer, 2015\. 746 p. ISBN 978-3-319-14141-1. Chapter 14\. Mining Time Series Data, P. 457-493. <https://doi.org/10.1007/978-3-319-14142-8>
  - Кильдишев Г.С., Френкель А.А. Анализ временных рядов и прогнозирование. М.: МИРЭА, 2021\. [https://www.elibrary.ru/item.asp?id=46489478](<http://xn--%20-eddibhwbrm2nzb.xn--q1a.xn--%2C%20%20-8yh5ca8dp1a0c2d5h.xn--80a.xn--%20%20%20%20%20-wlmam2adgvpuao7asjpfc7eybzalanezicc1b0ailg6tnlnh.xn--%20-med.xn--:%20%2C%202021-ytl5ixcwd5m.%20https//www.elibrary.ru/item.asp?id=46489478>)
  - Cryer J.D., Chan K.-S. Time Series Analysis with Applications in R. 2nd Edition. 506 p. ISBN: 978-0-387-75958-6
- *Дополнительная*
  - Imani S., Madrid F., Ding W., Crouter S.E., Keogh E.J. Introducing time series snippets: a new primitive for summarizing long time series // Data Min. Knowl. Discov. 2020\. Vol. 34, no. 6\. P. 1713-1743. <https://doi.org/10.1007/s10618-020-00702-y>
  - Nakamura T., Imamura M., Mercer R., Keogh E.J. MERLIN: Parameter-Free Discovery of Arbitrary Length Anomalies in Massive Time Series Archives // Proceedings of the 20th IEEE International Conference on Data Mining, ICDM 2020, Sorrento, Italy, November 17-20, 2020\. IEEE, 2020\. P. 1190-1195. <https://doi.org/10.1109/ICDM50108.2020.00147>
  - Rakthanmanon T., Campana B.J.L., Mueen A., Batista G.E.A.P.A., Westover M.B., Zhu Q., Zakaria J., Keogh E.J. Addressing Big Data Time Series: Mining Trillions of Time Series Subsequences Under Dynamic Time Warping // ACM Trans. Knowl. Discov. Data. 2013\. Vol. 7, no. 3\. P. 10:1-10:31. <https://doi.org/10.1145/2500489>
  - Zhu Y., Gharghabi S., Silva D.F., Dau H.A., Yeh C.-C.M., Senobari N.S., Almaslukh A., Kamgar K., Zimmerman Z., Funning G.J., Mueen A., Keogh E.J. The Swiss army knife of time series data mining: ten useful things you can do with the matrix profile and ten lines of code // Data Min. Knowl. Discov. 2020\. Vol. 34, no. 4\. P. 949-979. <https://doi.org/10.1007/s10618-019-00668-6>
  - Yankov D., Keogh E.J., Rebbapragada U. Disk aware discord discovery: finding unusual time series in terabyte sized datasets // Knowl. Inf. Syst. 2008\. Vol. 17, no. 2\. P. 241-262. <https://doi.org/10.1007/s10115-008-0131-9>
  - Yeh C.-C.M., Zhu Y., Ulanova L., Begum N., Dau H.A., Silva D.F., Mueen A., Keogh E.J. Matrix Profile I: All Pairs Similarity Joins for Time Series: A Unifying View That Includes Motifs, Discords and Shapelets // Proceedings of the IEEE 16th International Conference on Data Mining, ICDM 2016, December 12-15, 2016, Barcelona, Spain. IEEE, 2016\. P. 1317-1322. <https://doi.org/10.1109/ICDM.2016.0179>
  - Zhu Y., Imamura M., Nikovski D., Keogh E.J. Matrix Profile VII: Time Series Chains: A New Primitive for Time Series Data Mining // Proceedings of the 2017 IEEE International Conference on Data Mining, ICDM 2017, New Orleans, LA, USA, November 18-21, 2017\. IEEE, 2017\. P. 695-704. <https://doi.org/10.1109/ICDM.2017.79>

- [Балльно-рейтинговая система курса](https://edu.susu.ru/mod/resource/view.php?id=8719842)

- [Лист ознакомления с БРС](https://edu.susu.ru/mod/choice/view.php?id=8719843)

- [График контрольных мероприятий](https://edu.susu.ru/mod/resource/view.php?id=8719844)

- [Репозиторий курса](https://edu.susu.ru/mod/url/view.php?id=8719845)

Слайды презентаций к лекциям, файлы ноутбуков с заданиями, наборы данных

- [Объявления](https://edu.susu.ru/mod/forum/view.php?id=8719846)

- [Посещаемость](https://edu.susu.ru/mod/attendance/view.php?id=8719847)

- [Трансляция и видеозаписи лекций](https://edu.susu.ru/mod/url/view.php?id=8719848)

Подключение к трансляции лекций по ссылке <https://bbb.susu.ru/b/7vd-q27-h8h-ncc>

- [Практические занятия](https://edu.susu.ru/mod/bigbluebuttonbn/view.php?id=8719849)

## Создание репозитория

Создание копии репозитория курса, в которую будут загружаться решения задач практических работ в соответствии с заданиями.

**Создание копии репозитория курса <https://github.com/mzym/TimeSeriesCourse/>**

1\. Зарегистрируйтесь на портале [Github](https://github.com/)(если это не было сделано ранее).

2\. Перейдите в репозиторий по [ссылке](https://github.com/mzym/TimeSeriesCourse/), авторизуйтесь (если  это не было сделано ранее) и выполните **fork**:

**![](lecture/lecture-0-course-organization/github-fork-1.png)**

3\. Укажите имя репозитория в формате **Год**\-**Фамилия**-TimeSeriesCourse:

![](lecture/lecture-0-course-organization/github-fork-2.png)

4\. Поставьте "звезду" репозиторию (опционально, не влияет на баллы, выставляемые за выполнение заданий и тестов):

![](lecture/lecture-0-course-organization/github-fork-3.png)

## Базовые понятия

Базовые понятия:
временной ряд, подпоследовательность. Основные задачи интеллектуального анализа
временных рядов: поиск аномалий, поиск по образцу, поиск шаблонов, восстановление
пропусков, прогноз.

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719851)

[Видео лекции](https://bbb-proxy.susu.ru/playback/presentation/2.3/3c66a9b6d9d6eefa0df3367f171eb135d18dff55-1789039530455)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719852)

- [Базис-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719853)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Базис-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719855)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Базис-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719857)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Поиск по образцу

Мера динамической
трансформации времени (DTW, Dynamic Time Warping). Поиск на основе техники нижних границ.

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719859)

Видео лекции: [часть 1](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1758947985908), [часть 2](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1760099281274), [часть 3](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1760157755899), [часть 4](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1761367254344)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719860)

- [Поиск по образцу-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719861)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Поиск по образцу-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719863)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Поиск по образцу-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719865)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Поиск диссонансов

Понятие диссонанса. Алгоритм HotSAX. Понятие диапазонного диссонанса. Алгоритмы DRAG и MERLIN.

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719867)

Видео лекции: [часть 1](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1761372267430), [часть 2](https://bbb-proxy.susu.ru/playback/presentation/2.3/42bda19186679b2535897ee45f8ea687f85e3abd-1762576488329)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719868)

- [Диссонансы-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719869)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Диссонансы-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719871)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Диссонансы-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719873)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Матричный профиль ряда

Понятие матричного профиля. Применение матричного профиля для решения задач интеллектуального анализа временных рядов. Алгоритмы вычисления матричного профиля.

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719875)

Видео лекции: [часть 1](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1732336863312), [часть 2](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1733225425265)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719876)

- [Матричный профиль-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719877)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Матричный профиль-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719879)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Матричный профиль-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719881)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Поиск сниппетов

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719883)

[Видео лекции](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1733546670239)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719884)

- [Сниппеты-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719885)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Сниппеты-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719887)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Сниппеты-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719889)

**Сложность задания:** средняя (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Поиск цепочек

- [Слайды](https://edu.susu.ru/mod/url/view.php?id=8719891)

[Видео лекции](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1733482544547)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719892)

- [Цепочки-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719893)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 0.5-1 час

- [Цепочки-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719895)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 1-1.5 час

- [Цепочки-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719897)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 1.5-2 час

## Восстановление и прогноз

Аналитические алгоритмы восстановления временного ряда. Восстановление ряда с помощью нейронных сетей. Прогнозирование временных рядов с помощью модели ARIMA.

- [Слайды (Восстановление)](https://edu.susu.ru/mod/url/view.php?id=8719899)

[Видео лекции](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1734676148596)

- [Слайды (Прогноз)](https://edu.susu.ru/mod/url/view.php?id=8719900)

Видео лекции: [часть 1](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1734756197659), [часть 2](https://bbb-proxy.susu.ru/playback/presentation/2.3/594b73e28fdafb2db34858052874d3019d727a69-1735211513107)

- [Материалы для практической работы](https://edu.susu.ru/mod/url/view.php?id=8719901)

- [Восстановление Прогноз-УДОВЛ](https://edu.susu.ru/mod/assign/view.php?id=8719902)

**Сложность задания:** низкая (на оценку "удовлетворительно")
**Время выполнения:** 1.5-2 час

- [Восстановление Прогноз-ХОР](https://edu.susu.ru/mod/assign/view.php?id=8719904)

**Сложность задания:** средняя (на оценку "хорошо")
**Время выполнения:** 2-2.5 час

- [Восстановление Прогноз-ОТЛ](https://edu.susu.ru/mod/assign/view.php?id=8719906)

**Сложность задания:** высокая (на оценку "отлично")
**Время выполнения:** 3-4 час

## Тесты

- [Базис](https://edu.susu.ru/mod/quiz/view.php?id=8719908)

- [Поиск по образцу](https://edu.susu.ru/mod/quiz/view.php?id=8719909)

- [Диссонансы](https://edu.susu.ru/mod/quiz/view.php?id=8719910)

- [Матричный профиль](https://edu.susu.ru/mod/quiz/view.php?id=8719911)

- [Восстановление и прогноз](https://edu.susu.ru/mod/quiz/view.php?id=8719912)

## Промежуточная аттестация

- Экзамен
