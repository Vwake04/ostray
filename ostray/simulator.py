import random
import time
from threading import Thread
from ostray.lead import Lead
from ostray.lead import LeadProcessor

class Simulator:
    def __init__(
        self, 
        lead_processor: LeadProcessor, 
        interval=2
    ):
        self.lead_processor = lead_processor
        self.interval = interval
        self.lead_sources = ["Salesforce", "HubSpot"]
        self.personas = ["GPT-3", "BERT"]
        self.running = False

    def generate_lead(self):
        name = random.choice(self.personas)
        lead_source = random.choice(self.lead_sources)
        return Lead(name, lead_source)

    def start(self):
        self.running = True
        Thread(target=self._run).start()

    def stop(self):
        self.running = False

    def _run(self):
        while self.running:
            lead = self.generate_lead()
            print(f"Generated lead: {lead}")
            self.lead_processor.process_lead(lead)
            time.sleep(self.interval)

