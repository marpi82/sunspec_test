# sunspec_test
Wersja testowa skryptu odczytującego dane z urządzeń obsługujących protokół SunSpec(R)

# Uruchomienie
Do poprawnego uruchomienia skryptu potrzebna jest biblioteka pymodbus którą możemy zainstalować:
> pip3 install pymodbus
## Pobranie z GitHub
> git clone --recursive https://github.com/marpi82/sunspec_test.git
> cd modsunspec
## Parametry urządzenia sunspec
Należy wyedytować plik *test.py*
> nano test.py
i zmienić w 11 linii:
- *client_id* na odpowiedni wg dokumentacji falownika ID klienta sunspec/modbus
- *ipaddr*    na adres IP naszego falownika
- *ipport*    na port na którym mamy uruchomione protokół sunspec/modbus w falowniku (w większości przypadków jest to port 502)
Uruchomić skrypt:
> ./test.py
Skrypt wyświetla i zapisuje do pliku *result.txt* dane odczytane z falownika 
