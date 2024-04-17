# Домашние работы по MLOps
<details>
<summary style="font-size: 26px; font-weight: bold;">  HW_1 </summary>

### Цель задания
В этом задании вам предлагается решить простую и во многом учебную задачу по созданию автоматического конвейера проекта машинного обучения. 

Подобный подход с применением простых скриптов автоматизации для «склейки» отдельных частей конвейера используется в небольших проектах. 

Чаще же для автоматизации используется специализированное программное обеспечение, например, Jenkins.

### Содержание задания
Необходимо из «подручных средств» создать простейший конвейер для автоматизации работы с моделью машинного обучения. 

Отдельные этапы конвейера машинного обучения описываются в разных python–скриптах, 

которые потом соединяются (иногда используют термин «склеиваются») с помощью bash-скрипта.

### Этапы
- Создайте python-скрипт (data_creation.py), который создает различные наборы данных, описывающие некий процесс (например, изменение дневной температуры).

  Таких наборов должно быть несколько, в некоторые данные можно включить аномалии или шумы. 

  Часть наборов данных должна быть сохранена в папке «train», другая часть — в папке «test».


- Создайте python-скрипт (model_preprocessing.py), который выполняет предобработку данных, например с помощью sklearn.preprocessing.StandardScaler.


- Создайте python-скрипт (model_preparation.py), который создает и обучает модель машинного обучения на построенных данных из папки «train».


- Создайте python-скрипт (model_testing.py), проверяющий модель машинного обучения на построенных данных из папки «test».


- Напишите bash-скрипт (pipeline.sh), последовательно запускающий все python-скрипты.
</details>