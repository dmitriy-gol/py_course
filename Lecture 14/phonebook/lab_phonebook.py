import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Contact: {self.name}:{self.phone}"


class Phone:
    def __init__(self):
        self.contacts = []

    def show(self):
        """Метод для вывода контактов"""

        print("Список контактов:")
        for contact in self.contacts:
            print(contact)

    def import_contacts_from_csv(self, file):
        """Метод для импорта контактов"""

        print("Импортирую контакты.")
        with open(file, newline = "") as csvfile:
            fieldnames = ["Name", "Phone"]
            reader = csv.DictReader(csvfile, fieldnames)

            for row in reader:
                self.contacts.append(PhoneContact(row["Name"], row["Phone"]))

        print("Импорт был успешен...")

    def export_contacts_to_csv(self, file):
        """Метод для экспорта контактов"""

        print("Экспортирую контакты.")
        with open(file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone])
        print("Экспорт был успешен...")

    def search_contacts(self):
        """Метод для поиска контакта"""

        phrase = input("Введите фразу: ")
        print("Поиск контакта по фразе")
        count = 0
        for contact in self.contacts:
            if (phrase.lower() in contact.name.lower()) or (phrase in contact.phone):
                print(f"Найден контакт: {contact.name} {contact.phone}")
                count += 1
        if count == 0:
            print("Контакт не найден.")

phone = Phone()
phone.import_contacts_from_csv("contacts.csv")
phone.show()
phone.search_contacts()
phone.export_contacts_to_csv("exported_contacts.csv")