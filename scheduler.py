from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import scrape_data
from cleaner import clean_data
from database import create_database, insert_data

scheduler = BlockingScheduler()

def run_pipeline():
    print("Running automated pipeline...")

    scrape_data()
    clean_data()

    create_database()
    insert_data()

    print("Pipeline completed")

scheduler.add_job(run_pipeline, 'interval', minutes=30)

if __name__ == "__main__":
    run_pipeline()
    scheduler.start()