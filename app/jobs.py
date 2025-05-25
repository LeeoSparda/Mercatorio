from apscheduler.schedulers.background import BackgroundScheduler

def revalidar_certidoes():
    print("Simulando revalidação automática de certidões...")

def iniciar_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(revalidar_certidoes, 'interval', hours=24)
    scheduler.start()
