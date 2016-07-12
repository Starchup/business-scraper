from googleplaces import GooglePlaces, types, lang
import csv
import sys
import unidecode

google_places = GooglePlaces('AIzaSyCGjlpc3LYhzBYGS0hjXpXDPvk_kaVs_IE')


def main():
    target = ''
    types = ''
    searcharea = 3200;

    #Location input
    choice = raw_input("What location would you like to search near? ")
    target = choice

    choice = ''
    while choice != 'q':
        # Let users know what they can do.
        print("\n[1] Laundry")
        print("[2] Establishment")
        print("[3] Car Dealership")
        print("[4] Car Rental")
        print("[5] Car Wash")
        print("[6] Dentist")
        print("[7] Doctor")
        print("[8] Finance")
        print("[9] Gym")
        print("[10] Hair Care")
        print("[11] Health")
        print("[12] Hospital")
        print("[13] Insurance Agency")
        print("[14] Lawyer")
        print("[15] Local Government Office")
        print("[16] Physiotherapist")
        print("[17] Spa")
        print("[18] Veterinary Care")
        print("[19] Enter a type")

        choice = input("What type would you like to filter by? ")

        # Respond to the user's choice.
        if choice == 1:
            types = 'laundry'
            break
        elif choice == 2:
            types = 'beauty_salon'
            break
        elif choice == 3:
            types = 'car_dealer'
            break
        elif choice == 4:
            types = 'car_rental'
            break
        elif choice == 5:
            types = 'car_wash'
            break
        elif choice == 6:
            types = 'dentist'
            break
        elif choice == 7:
            types = 'doctor'
            break
        elif choice == 8:
            types = 'finance'
            break
        elif choice == 9:
            types = 'gym'
            break
        elif choice == 10:
            types = 'hair_care'
            break
        elif choice == 11:
            types = 'health'
            break
        elif choice == 12:
            types = 'hospital'
            break
        elif choice == 13:
            types = 'insurance_agency'
            break
        elif choice == 14:
            types = 'lawyer'
            break
        elif choice == 15:
            types = 'local_government_office'
            break
        elif choice == 16:
            types = 'physiotherapist'
            break
        elif choice == 17:
            types = 'spa'
            break
        elif choice == 18:
            types = 'veterinary_care'
            break
        elif choice == 19:
            types = raw_input("Type: ")
            break
        else:
            break

    searcharea = input("How large of a radius would you like to search? ")

    # helper to format the incomming google place data into csv
    def getPlaceData(place):
        data = [];
        data.append(place.name)
        data.append(place.vicinity)
        data.append(place.place_id)

        # The following method has to make a further API call.
        place.get_details()
        if (place.local_phone_number):
            data.append(place.local_phone_number)
        if (place.international_phone_number):
            data.append(place.international_phone_number)
        if (place.website):
            data.append(place.website)
        if (place.url):
            data.append(place.url)
        #print(place.name)
        return [data]

    def getMorePlaces(target, types, searcharea, token=None):
        return google_places.nearby_search(location=target,
                                        lat_lng=None,
                                        radius=searcharea,
                                        types=types,
                                        pagetoken=token)

    def outputPlaces(csv, places):
        #print("must output " + str(len(places)))
        print("Loading...")
        for place in places:
            csv.writerows(getPlaceData(place))

    # get ready to write
    with open('data.csv', 'a') as fp:
        a = csv.writer(fp, delimiter=',')

        # write csv headers
        a.writerows([['Name',
            'Vicinity',
            'Place Id',
            'Local Phone',
            'Intl Phone',
            'Website',
            'Google Place']])

        # Add city name & extra lines for clarity
        a.writerows([[]])
        a.writerows([[target]])
        a.writerows([[]])

        try:
            query_result = getMorePlaces(target, types, searcharea)
            outputPlaces(a, query_result.places)

            while (query_result.next_page_token is not None):
                query_result = getMorePlaces(target, types, searcharea, query_result.next_page_token)
                outputPlaces(a, query_result.places)

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)

    print("Finished!")

main();
