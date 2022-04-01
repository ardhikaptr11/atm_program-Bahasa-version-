import random
import datetime
from customer import Customer

print('Arta Finanace, Ltd.')
print('===================')

atm = Customer(id)

user_info = {
    "cust_pin": int(atm.checkPin())
}

while True: 
    id = input("Masukkan PIN: ")
    while len(id) != 6 or (not id.isdigit()):
        print('\nHINT: PIN terdiri dari 6 digit angka\n')
        id = input("Masukkan PIN: ")
    id = int(id)

    while id != user_info['cust_pin']:
        print('\nPIN anda salah...\n')
        id = input("Masukkan PIN: ")
        while len(id) != 6 or (not id.isdigit()):
            id = input("Masukkan PIN: ")
        id = int(id)
    
    while True: 
        print('\nSelamat datang di layanan Arta Finance, Ltd., silahkan pilih menu.')
    
        print('\n 1 - Cek Saldo \n 2 - Debet \n 3 - Simpan \n 4 - Ganti Pin \n 5 - Keluar')

        selectmenu = int(input('\nSilahkan pilih menu: '))

        if selectmenu == 1:
            input_pin = int(input('Masukkan PIN: '))
            message_success = f'\nJumlah saldo anda saat ini: Rp {atm.checkBalance():,}'
            message_fail = '\nPIN yang anda masukkan salah.'
            if input_pin == user_info['cust_pin']:
                print(message_success)
            else:
                print(message_fail)
        
        elif selectmenu == 2:
            print('\n1. Utamakan Rp 50,000\n2. Utamakan Rp 100,000\n3. Batal')
            user_input = int(input('Masukkan hanya kode angka untuk melanjutkan: '))

            if user_input == 1: 
                nominal_input = int(input('\nMasukkan jumlah nominal: '))
                message = f'Anda akan melakukan penarikan dengan nominal berikut? Rp {nominal_input:,}'
                option = '1. Yes\n2. No'
                if nominal_input % 50000 == 0 and nominal_input < atm.checkBalance():
                    print(message)
                    print(option)
                    user_confirm = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
                    if user_confirm == 1:
                        input_pin = int(input('Masukkan PIN: '))
                        if input_pin == user_info['cust_pin']:     
                            atm.withdrawBalance(nominal_input)
                            print('\nTransaksi berhasil!')
                            print(f'Sisa saldo anda: Rp {atm.checkBalance():,}')
                        else:
                            print('PIN yang anda masukkan salah.')
                    elif user_confirm == 2:
                        print('Transaksi dibatalkan.')
                        print('Kembali ke menu awal...')
                else:
                    print('\nSaldo anda tidak mencukupi untuk melakukan transaksi.')
                    print('Silahkan lakukan penambahan saldo.')
            
            if user_input == 2:
                nominal_input = int(input('\nMasukkan jumlah nominal: '))
                if nominal_input % 100000 == 0 and nominal_input >= atm.checkBalance():
                    print('\nSaldo anda tidak mencukupi untuk melakukan transaksi.')
                    print('Silahkan lakukan penambahan saldo.')
                elif nominal_input % 100000 != 0: 
                    print('\nPERINGATAN: Berlaku kelipatan Rp 100,000\n')
                    retry_input = int((input('Masukkan jumlah nominal: ')))
                    while retry_input % 100000 != 0:
                        retry_input = int(input('Masukkan jumlah nominal: '))
                    if retry_input % 100000 == 0 and retry_input < atm.checkBalance():
                        print(f'Anda akan melakukan penarikan dengan nominal berikut? Rp {retry_input:,}')
                        print(option)
                        user_confirm = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
                        if user_confirm == 1:
                            input_pin = int(input('Masukkan PIN: '))
                            message_success = '\nTransaksi berhasil!'
                            if input_pin == user_info['cust_pin']:
                                atm.withdrawBalance(retry_input)
                                print(message_success)
                                print(f'Sisa saldo anda: Rp {atm.checkBalance():,}') 
                            else:
                                print('PIN yang anda masukkan salah.')
                        elif user_confirm == 2:
                            print('Transaksi dibatalkan')
                            print('Kembali ke menu awal...')
                    else: 
                        print('\nSaldo anda tidak mencukupi untuk melakukan transaksi.')
                        print('Silahkan lakukan penambahan saldo.')
                else:
                    print(f'Anda akan melakukan penarikan dengan nominal berikut? Rp {nominal_input:,}')
                    print(option)
                    user_confirm = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
                    if user_confirm == 1:
                        input_pin = int(input('Masukkan PIN: '))
                        if input_pin == user_info['cust_pin']:
                            atm.withdrawBalance(nominal_input)
                            print('Transaksi berhasil!')
                            print(f'Sisa saldo anda: Rp {atm.checkBalance():,}')
                        else:
                            print('PIN yang anda masukkan salah.')
                    elif user_confirm == 2:
                        print('Transaksi dibatalkan')
                        print('Kembali ke menu awal...')
            
            if user_input == 3:
                print('Kembali ke menu awal...')

        elif selectmenu == 3:
            print('\nBerlaku kelipatan Rp 50,000\n')
            nominal_input = int(input('Masukkan nominal saldo: '))
            message = f'Anda akan melakukan penarikan dengan nominal berikut? Rp {nominal_input:,}'
            option = '1. Yes\n2. No'
            if nominal_input < 50000 or nominal_input % 50000 != 0:
                retry_input = int(input('Masukkan nominal saldo: '))
                while retry_input < 50000 or retry_input % 50000 != 0:
                    retry_input = retry_input = int(input('Masukkan nominal saldo: '))
                if True:
                    atm.depositBalance(retry_input)
                    print(f'Anda akan melakukan penarikan dengan nominal berikut? Rp {retry_input:,}')
                    print(option)
                    user_confirm = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
                    if user_confirm == 1:
                        input_pin = int(input('Masukkan PIN: '))
                        if input_pin == user_info['cust_pin']:
                            print('\nTransaksi Berhasil!')
                            print(f'Saldo anda sekarang: Rp {atm.checkBalance():,}')
                        else:
                            print('PIN yang anda masukkan salah.')
            elif nominal_input % 50000 == 0:
                print(message)
                print(option)
                user_confirm = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
                if user_confirm == 1:
                    input_pin = int(input('Masukkan PIN: '))
                    if input_pin == user_info['cust_pin']:
                        atm.depositBalance(nominal_input)
                        print('\nTransaksi Berhasil!')
                        print(f'Saldo anda sekarang: Rp {atm.checkBalance():,}')
                    else:
                        print('PIN yang anda masukkan salah.')

                
            elif nominal_input > 10000000:
                print('Batas deposit harian Rp 10,000,000')

        elif selectmenu == 4: 
            message = 'Apakah anda yakin ingin melakukan penggantian PIN ?'
            print(message)
            option = '1. Yes\n2. No'
            print(option)
            user_input = int(input('Masukkan hanya kode angka untuk melanjutkan: '))
            if user_input == 1:
                current_pin = int(input('Masukkan PIN lama: '))
                if current_pin == int(user_info['cust_pin']): 
                    print('\nTunggu sebentar...\n')
                    new_pin = input('Masukkan 6 digit PIN baru: ')
                    while len(new_pin) != 6 or (not new_pin.isdigit()):
                        new_pin = input('Masukkan 6 digit PIN baru: ')
                    new_pin = int(new_pin)
                    verify_pin = int(input('Masukkan ulang 6 digit PIN baru: '))
                    if verify_pin == new_pin:
                        print('\nPIN berhasil diubah!')
                        user_info.update({'cust_pin':verify_pin})
                    else: 
                        verify_pin_fail = int(input('PIN tidak cocok ! Masukkan ulang PIN baru: '))
                        trial = 1
                        while verify_pin_fail != new_pin and trial < 3:
                            verify_pin_fail = int(input('PIN tidak cocok ! Masukkan ulang PIN baru: '))
                            trial += 1
                        if trial != 3:
                            print('\nPIN berhasil diubah!')
                            user_info.update({'cust_pin':verify_pin_fail})
                        else:
                            print('\nPIN salah, silahkan coba lagi!')
                else:
                    print('\nPIN salah, silahkan coba lagi!')
            elif user_input == 2:
                print('\nKembali ke menu awal...')
                   
        elif selectmenu == 5:
            print('\nResi tercetak otomatis saat anda keluar. \nHarap simpan tanda terima ini sebagai bukti transaksi anda.\n')
            print('Record No: ', random.randint(10000, 1000000))
            print('Tanggal: ',  datetime.datetime.now())
            print(f'Informasi akhir salo: Rp {atm.checkBalance():,}')
            print('\nTerimakasih telah menggunakan layanan kami! (Arta Finance, Ltd.)')
            exit()
        else:
            print('Maaf menu belum tersedia saat ini.')