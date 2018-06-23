# crm_working

Модели
Организация:
	название
	почта
	контактное лицо
	вид деятельности

Вакансия:
	id организации Foreign key
	название задачи
	описание задачи
	граничный срок
	id работника Foreign key
	статус


Состояние вакансии:
	id вакансии
	id работника
	подтверждение роботника
	подтверждение заказчиком
	

Работник:
	имя
	почта
	скилы
	статус
	рейтинг

Скилл_работника(Many to Many):
	id работника
	id скилла
	опыт
	
Скилл:
	название

Функционал
Новая задача:
	Форма: название, описание, срок, поиск роботника по скилам или разослать всем свободным.
	Рассылка работникам, с вариантами отклонить, принять. Возвращаем заказчику список всех 		принявшых предложение, он выбирает исполнителя. Выбраному подтверждение, всем остальным 	отказ.
