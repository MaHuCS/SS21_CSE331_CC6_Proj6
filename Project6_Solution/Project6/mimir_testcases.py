import unittest
import random
from Project6.hashtable import HashTable, HashNode, CataData

random.seed(331)


class TestProject1(unittest.TestCase):

    def test_hash(self):
        # (1) Basic with no double hashing
        table1 = HashTable(capacity=16)

        self.assertEqual(4, table1.hash("Ian"))
        self.assertEqual(2, table1.hash("Max"))
        self.assertEqual(5, table1.hash("Yash"))
        self.assertEqual(0, table1.hash("Brandon"))

        # (2) Basic with double hashing - Inserting Mode Only
        table2 = HashTable(capacity=16)

        table2.table = [None, None, None, None, HashNode("Ian", 150, True),
                        None, None, None, HashNode("H", 100),
                        None, None, None, None, None, None, None]

        self.assertEqual(9, table2.hash("Andrew", inserting=True))
        self.assertEqual(5, table2.hash("Andy", inserting=True))
        self.assertEqual(15, table2.hash("Lukas", inserting=True))

        # (3) Larger with Inserting and not Inserting
        table3 = HashTable(capacity=16)

        table3.table = [None, None, None,
                       HashNode('class_ever', 1), HashNode(None, None, True),
                       HashNode(None, None, True), None, None, None,
                       None, HashNode(None, None, True), None,
                       None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        self.assertEqual(4, table3.hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(15, table3.hash("is_the"))

        # Should insert in the first available bin
        self.assertEqual(5, table3.hash("yash", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(7, table3.hash("yash"))

        self.assertEqual(3, table3.hash("class_ever"))

        # (4) Large Comprehensive
        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i*10 for i in range(19)]

        table4 = HashTable(capacity=16)

        table4.table = [None, None, HashNode('Max', 0),
                        None, HashNode('Ian', 10),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode(None, None, True), None]

        expected = [2, 2, 4, 4, 9, 9, 8, 8, 8, 8, 0, 0, 8, 8, 7, 7, 6, 6, 15, 15, 3, 3, 15, 15, 14, 7, 9, 9, 1, 1, 9,
                    9, 0, 0, 5, 8, 15, 15]

        for i, key in enumerate(keys):
            # inserts every key in inserting mode and normal mode
            self.assertEqual(expected[2*i], table4.hash(key, inserting=True))
            self.assertEqual(expected[2*i + 1], table4.hash(key))

    def test_setitem(self):
        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)
        assert (solution == table.table)

    def test_getitem(self):
        table = HashTable()

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)
        assert (solution == table.table)

        for i in solution:
            if i:
                assert (table[i.key] == i.value)

    def test_delitem(self):
        table = HashTable()

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None,
                         None,
                         HashNode(None, None), None, None, None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)

        assert (pre_solution == table.table)

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        assert (post_solution == table.table)
        print(table)

    def test_contains(self):
        table = HashTable()
        assert ('key' in table) == False

        table['key'] = 7

        assert ('key' in table) == True
        assert ('new_key' in table) == False

    def test_update(self):
        table = HashTable()

        table["birds"] = 10
        table["real"] = 15

        table.update([("aren't", 20), ("real", 8)])

        assert table["aren't"] == 20
        assert table["real"] == 8

    def test_keys_values_items(self):
        table = HashTable()

        initial_keys = ['one', 'two', 'three']
        initial_values = [1, 2, 31]
        initial_items = [('one', 1), ('two', 2), ('three', 31)]

        for i in range(3):
            table[initial_keys[i]] = initial_values[i]

        keys = table.keys()
        values = table.values()
        items = table.items()

        assert set(initial_keys) == set(keys)
        assert set(initial_values) == set(values)
        assert set(initial_items) == set(items)

    def test_clear(self):
        table = HashTable()

        table['table'] = 1
        table['will'] = 2
        table['be'] = 3
        table['cleared'] = 4

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

        table['one'] = 1

        table.clear()

        assert table.size == 0
        for node in table.table:
            assert node is None

    def test_all(self):
        table = HashTable()

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None), None, None, None, None,
                         None, HashNode(None, None), None, None, None, HashNode('cse331', 100), None]

        table['cse331'] = 100
        table['is_the'] = 3005

        assert (table.size == 2)
        assert (table.capacity == 8)

        table['best'] = 42
        table['class_ever'] = 1

        assert (table.size == 4)
        assert (table.capacity == 16)
        print(table)

        assert (pre_solution == table.table)

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        assert (post_solution == table.table)
        print(table)

        with self.assertRaises(KeyError):
            print(table['best'])

    def test_cata_query(self):
        cata_data = CataData()

        cata_data.enter("Ian", "Wilson", 1)
        cata_data.exit("Ian", "Akers", 4)
        expected = 3.0
        student_response = cata_data.get_average("Wilson", "Akers")
        self.assertAlmostEqual(expected, student_response)

        cata_data = CataData()

        cata_data.enter("Ian", "Wilson", 1)
        cata_data.enter("Max", "Wilson", 1)
        cata_data.exit("Ian", "Akers", 4)
        cata_data.exit("Max", "Akers", 5)
        expected = 3.5
        student_response = cata_data.get_average("Wilson", "Akers")
        self.assertAlmostEqual(expected, student_response)

        cata_data = CataData()

        cata_data.enter("Ian", "Engineering", 0)
        cata_data.enter("Max", "Chemistry", 7)
        cata_data.exit("Ian", "Chemistry", 1)
        cata_data.enter("Ian", "Chemistry", 4)
        cata_data.exit("Ian", "Wells", 6)
        cata_data.enter("Ian", "Wells", 8)
        cata_data.exit("Ian", "Wilson", 10)
        cata_data.exit("Max", "Wells", 12)

        expected = 3.5
        student_response = cata_data.get_average("Chemistry", "Wells")
        self.assertAlmostEqual(expected, student_response)

        expected = 1.0
        student_response = cata_data.get_average("Engineering", "Chemistry")
        self.assertAlmostEqual(expected, student_response)

        expected = 0.0
        student_response = cata_data.get_average("Akers", "Anthony")
        self.assertAlmostEqual(expected, student_response)

    def test_cata_query_large(self):
        bus_stops = ["Wilson", "Case", "Wonders", "IM West", "Wells", "1855",\
            "Spartan Stadium", "Anthony", "Engineering", "Bessey", "Grand River", "Union",\
                "Akers", "IM East", "Natural Resources", "Lot 89", "Biochemistry", "SnyPhy",\
                    "Landon", "Brody", "Breslin", "CommArtSci", "VetMed"]
        answers = [15.333333333333334, 9.0, 19.0, 35.0, 42.0, 27.0, 12.0, 31.0, \
            33.0, 14.5, 16.5, 28.5, 7.0, 12.0, 22.0, 15.333333333333334, 33.0, \
            10.0, 16.5, 24.0, 31.0, 12.5, 6.0, 1.0, 12.0, 11.5, 33.0, 19.0, \
            31.0, 6.0, 32.5, 32.5, 12.0, 43.0, 7.0, 36.0, 12.0, 23.333333333333332, \
            12.0, 30.0, 28.0, 20.0, 17.0, 38.0, 20.0, 30.0, 18.0, 22.0, 28.5, 19.0, \
            39.5, 19.0, 26.0, 39.0, 23.0, 19.0, 26.0, 43.0, 15.333333333333334, 15.0, \
            30.0, 40.0, 14.0, 23.333333333333332, 31.0, 28.0, 12.5, 17.5, 12.0, 11.0, \
            24.0, 29.666666666666668, 33.0, 17.0, 44.0, 13.0, 5.0, 16.0, 38.0, 31.0, \
            24.0, 33.0, 25.0, 32.0, 20.0, 33.0, 19.0, 14.0, 25.5, 34.0, 10.0, 2.0, \
            28.0, 27.0, 8.0, 1.0, 26.0, 37.0, 17.5, 25.333333333333332, 34.0, 44.0, \
            41.0, 44.0, 29.0, 11.0, 34.0, 19.0, 27.0, 19.5, 20.0, 41.0, 19.0, 17.0, \
            14.0, 18.0, 25.5, 17.0, 4.0, 38.0, 39.0, 29.0, 29.666666666666668, 36.0, \
            18.0, 30.0, 21.0, 31.5, 41.0, 29.0, 2.0, 24.0, 8.0, 21.0, 33.5, 28.0, 42.0, \
            15.0, 21.0, 25.5, 22.0, 19.0, 37.0, 30.0, 23.5, 27.0, 1.0, 20.0, 25.0, 35.0, \
            22.0, 30.0, 22.5, 23.0, 23.333333333333332, 6.0, 32.0, 22.0, 32.0, 18.0, 6.0, \
            24.0, 18.0, 22.0, 43.0, 16.0, 18.0, 6.0, 13.0, 25.333333333333332, 35.0, 36.0, \
            43.0, 14.0, 9.0, 29.666666666666668, 15.0, 24.0, 11.5, 36.0, 41.0, 43.0, 26.0, \
            11.0, 6.0, 2.0, 25.333333333333332, 24.0, 1.0, 10.0, 39.5, 40.0, 39.5, 27.0, \
            39.5, 42.0, 8.0, 33.0, 29.0, 4.0, 15.0, 9.0, 35.0, 41.0, 45.0, 19.5, 14.5, 43.5, \
            23.0, 23.5, 14.0, 26.0, 31.5, 5.0, 5.0, 43.5, 1.0, 5.0, 40.0, 4.0, 8.0, 12.0, \
            15.0, 33.5, 20.0, 24.0, 26.0, 41.0, 25.5, 35.0, 12.0, 44.0, 32.0, 18.0, 14.0, \
            29.0, 21.0, 8.0, 22.5, 24.0, 16.0, 27.0, 4.0, 20.0, 3.0, 12.0, 20.0, 26.0, 45.0, 40.0]
        # Keeps track of trips taken
        trips = list()
        # Used to store the starting bus stop of an entry with its enter time
        stations_and_time = list()

        cata_data = CataData()
        for i in range(250):
            # Random bus stop
            start_pos = random.randint(0, 1000) % len(bus_stops)
            # Random start time
            start_time = random.randint(0, 1000)
            cata_data.enter(str(i), bus_stops[start_pos], start_time)
            stations_and_time.append((start_pos, start_time))
        
        for i in range(250):
            # Get the start time
            start_pos, start_time = stations_and_time[i]
            dest_pos = random.randint(0, 1000) % len(bus_stops)
            while dest_pos == start_pos:
                # Ensures random destination station is different from origin
                dest_pos = random.randint(0, 1000) % len(bus_stops)
            # Trip end time will be somewhere between 1 and 45 after start time
            end_time = start_time + random.randint(1, 45)
            cata_data.exit(str(i), bus_stops[dest_pos], end_time)
            trips.append((bus_stops[start_pos], bus_stops[dest_pos]))

        for i in range(len(answers)):
            student = cata_data.get_average(trips[i][0], trips[i][1])
            self.assertAlmostEqual(answers[i], student)

if __name__ == '__main__':
    unittest.main()
