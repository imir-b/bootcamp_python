import time

BAR_LENGTH = 40

def ft_progress(lst):
    total = len(lst)
    
    for i, element in enumerate(lst, 1):
        pourcentage = i / total
        blocs_remplis = int(BAR_LENGTH * pourcentage)
        barre = '█' * blocs_remplis + ' ' * (BAR_LENGTH - blocs_remplis)
        
        print(f"\rProgression |{barre}| {pourcentage * 100:.1f}% ({i}/{total})", end="", flush=True)
        
        yield element
        
    print()

def main():
    for element in ft_progress(lst := range(100)):
        time.sleep(0.1)  # Simule un traitement long pour chaque élément

if __name__ == "__main__":
    main()