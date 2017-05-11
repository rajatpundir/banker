##################################################################
# BEGIN Class Account
class Account:
	'Account class'
	##############################################################
	def __init__(self, database):
		# CONNECT TO DATABASE
		self.conn = sqlite3.connect(database)
	##############################################################
	def create_table(self):
		# CREATE ACOOUNT TABLE
		self.conn.execute('''CREATE TABLE AACOUNT(
			ACCOUNT_ID		INTEGER,
			FOREIGN KEY(ACCOUNT_ID)	REFERENCES CUSTOMER(CUSTOMER_ID),
			ACCOUNT_TYPE 	INTEGER,
			BALANCE			REAL,
			WITHDRAWALS		INTEGER,
			CLOSED_TIME		TEXT
			);''')
		print "Account Table created successfully";
	##############################################################
	def insert_account(self, account_id, account_type, balance):
		# INSERT ROW
		self.conn.execute("INSERT INTO CUSTOMER (ACCOUNT_ID, ACCOUNT_TYPE, BALANCE, WITHDRAWALS, CLOSED_TIME) VALUES (:1, :2, :3, 0, NULL)", (account_id, account_type, balance));
		self.conn.commit()
	##############################################################
	def select_all(self):
		# SELECT ROWS
		cursor = self.conn.execute("SELECT *  from ACCOUNT")
		for row in cursor:
		   print "ACCOUNT_ID = ", row[0]
		   print "ACCOUNT_TYPE = ", row[1]
		   print "BALANCE = ", row[2]
		   print "WITHDRAWALS = ", row[3]
		   print "CLOSED_TIME = ", row[4], "\n"
	##############################################################
	def delete_all(self, database):
		# DELETE ROWS
		cursor = self.conn.execute("SELECT *  from ACCOUNT")
		for row in cursor:
		   self.delete_customer(database, row[0])
	##############################################################
	def update_balance(self, account_id, balance):
		# UPDATE PASSWORD
		self.conn.execute("UPDATE ACCOUNT set BALANCE = :1 where ACCOUNT_ID = :2", (balance, account_id))
		self.conn.commit
	##############################################################
	def delete_account(self, database, account_id):
		# DELETE ROWS
		conn = sqlite3.connect(database)
		self.conn.execute("DELETE from ACCOUNT where ACCOUNT_ID = :1;", (str(account_id),))
		self.conn.commit()
	##############################################################
	def close(self):
		# CLOSE CONNECTION
		self.conn.close()
# END Class Account
##################################################################