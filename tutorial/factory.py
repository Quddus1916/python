import concrete_impl

def Factory(languages):
    localizers = {
        "French": concrete_impl.FrenchLocalizer,
        "Spanish": concrete_impl.SpanishLocalizer,
    }
    my_instances = []
    for language in languages:
        my_instances.append(localizers[language]())

    return my_instances
    

if __name__ == "__main__":

    languages = ["French","Spanish"]
    instances = Factory(languages)
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        for instance in instances:
            print(instance.localize(msg))


