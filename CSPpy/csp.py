from typing import Any
from queue import Queue
from collections import deque


class CSP:
    def __init__(
        self,
        variables: list[str],
        domains: dict[str, set],
        edges: list[tuple[str, str]],
    ):
        # Constructs a CSP instance with the given variables, domains and edges.
        
        # Parameters
        variables = variables
            # The variables for the CSP
        domains = domains
            # The domains of the variables
        self.edges = edges
            # Pairs of variables that must not be assigned the same value
       
        self.variables = variables
        self.domains = domains

        # Binary constraints as a dictionary mapping variable pairs to a set of value pairs.
        #
        # To check if variable1=value1, variable2=value2 is in violation of a binary constraint:
        # if (
        #     (variable1, variable2) in self.binary_constraints and
        #     (value1, value2) not in self.binary_constraints[(variable1, variable2)]
        # ) or (
        #     (variable2, variable1) in self.binary_constraints and
        #     (value1, value2) not in self.binary_constraints[(variable2, variable1)]
        # ):
        #     Violates a binary constraint
        self.binary_constraints: dict[tuple[str, str], set] = {}
        for variable1, variable2 in edges:
            self.binary_constraints[(variable1, variable2)] = set()
            for value1 in self.domains[variable1]:
                for value2 in self.domains[variable2]:
                    if value1 != value2:
                        self.binary_constraints[(variable1, variable2)].add((value1, value2))
                        self.binary_constraints[(variable1, variable2)].add((value2, value1))

    def ac_3(self) -> bool:
        """Performs AC-3 on the CSP.
        Meant to be run prior to calling backtracking_search() to reduce the search for some problems.
        
        Returns
        -------
        bool
            False if a domain becomes empty, otherwise True
        """
        # Inizializza la coda con tutti gli archi
        queue = deque(self.edges)
        
        # Finché ci sono archi da controllare
        while queue:
            (X, Y) = queue.popleft()
            
            # Controlla se il dominio di X può essere ridotto rispetto a Y
            if self.revise(X, Y):
                # Se il dominio di X è vuoto, il problema è insoddisfacibile
                if not self.domains[X]:
                    return False
                
                # Se X è cambiato, aggiungi tutti gli archi (Z, X) dove Z è vicino a X
                for Z in self.neighbors(X):
                    if Z != Y:
                        queue.append((Z, X))
        
        return True  # Il CSP è arc-consistente
        


    def revise(self, X, Y):
        """Rivedi il dominio di X rispetto a Y. Ritorna True se il dominio di X è cambiato."""
        revised = False
        
        # Copia temporanea dei valori di X da esaminare
        for x in set(self.domains[X]):
            # Controlla se esiste un valore y in Y che soddisfa i vincoli con x
            if not any((x, y) in self.binary_constraints[(X, Y)] for y in self.domains[Y]):
                # Se non c'è un tale valore, rimuovi x dal dominio di X
                self.domains[X].remove(x)
                revised = True
        
        return 
    

    def neighbors(self, var: str) -> list[str]:
        """Restituisce una lista di variabili vicine a 'var'."""
        neighbors = []
        for (X, Y) in self.edges:
            if X == var:
                neighbors.append(Y)
            elif Y == var:
                neighbors.append(X)
        return neighbors


    def backtracking_search(self) -> None | dict[str, Any]:
        """Performs backtracking search on the CSP.
        
        Returns
        -------
        None | dict[str, Any]
            A solution if any exists, otherwise None
        """
        def backtrack(assignment: dict[str, Any]):
            if len(assignment) == len(self.variables):
                return assignment
        
            # Seleziona una variabile non ancora assegnata
            var = self.select_unassigned_variable(assignment)
            
            # Prova ogni valore nel dominio della variabile
            for value in self.domains[var]:
                # Verifica se l'assegnazione è valida
                if self.is_consistent(var, value, assignment):
                    # Assegna il valore alla variabile
                    assignment[var] = value
                    
                    # Continua la ricerca con l'assegnazione aggiornata
                    result = backtrack(assignment)
                    
                    # Se trovi una soluzione, restituiscila
                    if result is not None:
                        return result
                    
                    # Se non trovi una soluzione, rimuovi l'assegnazione (backtrack)
                    del assignment[var]
            
            # Se nessuna assegnazione funziona, torna indietro
            return None
        
        # Avvia la ricerca con un'assegnazione vuota
        return backtrack({})
    

    def select_unassigned_variable(self, assignment: dict[str, Any]) -> str:
        """Select a variable not assigned yet.

        Parameters
        ----------
        assignment : dict[str, Any]

        Returns
        -------
        str
            The variable not assigned yet.
        """
        for var in self.variables:
            if var not in assignment:
                return var
        raise Exception("Non ci sono variabili non assegnate")
    

    def is_consistent(self, var: str, value: Any, assignment: dict[str, Any]) -> bool:
        """Controlla se l'assegnazione di 'value' a 'var' è consistente con i vincoli.

        Parameters
        ----------
        var : str
            La variabile da assegnare.
        value : Any
            Il valore da assegnare.
        assignment : dict[str, Any]
            L'assegnazione parziale attuale.

        Returns
        -------
        bool
            True se l'assegnazione è consistente, False altrimenti.
        """
        # Controlla i vincoli con tutte le variabili già assegnate
        for other_var, other_value in assignment.items():
            if (var, other_var) in self.binary_constraints:
                if (value, other_value) not in self.binary_constraints[(var, other_var)]:
                    return False
            elif (other_var, var) in self.binary_constraints:
                if (other_value, value) not in self.binary_constraints[(other_var, var)]:
                    return False
        return True


def alldiff(variables: list[str]) -> list[tuple[str, str]]:
    """Returns a list of edges interconnecting all of the input variables
    
    Parameters
    ----------
    variables : list[str]
        The variables that all must be different

    Returns
    -------
    list[tuple[str, str]]
        List of edges in the form (a, b)
    """
    return [(variables[i], variables[j]) for i in range(len(variables) - 1) for j in range(i + 1, len(variables))]
