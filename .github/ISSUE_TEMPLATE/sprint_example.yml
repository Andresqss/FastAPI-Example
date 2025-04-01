name: Scrum Ticket
description: Crea un nuevo ticket para el backlog de Scrum
title: "[TICKET]: "
labels: ["backlog"]
assignees: []

body:
  - type: input
    id: id
    attributes:
      label: "ID del Ticket"
      description: "Identificador único del ticket (se genera automáticamente o se puede dejar en blanco)."
      placeholder: "Ejemplo: SCRUM-001"
  
  - type: input
    id: title
    attributes:
      label: "Título"
      description: "Breve resumen del ticket."
      placeholder: "Ejemplo: Implementar la autenticación de usuario"

  - type: dropdown
    id: type
    attributes:
      label: "Tipo de Ticket"
      description: "Selecciona el tipo de ticket."
      options:
        - Historia de Usuario
        - Tarea
        - Bug
        - Spike
        - Mejora
      default: 0

  - type: textarea
    id: description
    attributes:
      label: "Descripción"
      description: "Explicación detallada del ticket."
      placeholder: "Describe el contexto, el problema a resolver o la funcionalidad a implementar."
  
  - type: textarea
    id: acceptance_criteria
    attributes:
      label: "Criterios de Aceptación"
      description: "Lista de condiciones que deben cumplirse para considerar el ticket completado."
      placeholder: "- [ ] El usuario puede iniciar sesión con credenciales válidas\n- [ ] Se muestra un mensaje de error si las credenciales son incorrectas"
  
  - type: textarea
    id: definition_of_done
    attributes:
      label: "Definición de Hecho (DoD)"
      description: "Condiciones para que el ticket sea considerado terminado."
      placeholder: "- [ ] Código revisado y aprobado\n- [ ] Pruebas automatizadas pasadas\n- [ ] Desplegado en ambiente de staging"

  - type: dropdown
    id: priority
    attributes:
      label: "Prioridad"
      description: "Nivel de importancia del ticket."
      options:
        - Alta
        - Media
        - Baja
      default: 1

  - type: dropdown
    id: status
    attributes:
      label: "Estado"
      description: "Estado actual del ticket en el flujo de trabajo."
      options:
        - To Do
        - In Progress
        - In Review
        - Done
      default: 0

  - type: input
    id: sprint
    attributes:
      label: "Sprint"
      description: "Número del sprint en el que se trabajará este ticket."
      placeholder: "Ejemplo: Sprint 5"

  - type: input
    id: assignee
    attributes:
      label: "Responsable"
      description: "Persona asignada a este ticket."
      placeholder: "Ejemplo: @usuario"

  - type: textarea
    id: tags
    attributes:
      label: "Etiquetas"
      description: "Categorías o áreas de impacto (separadas por comas)."
      placeholder: "Ejemplo: frontend, autenticación, seguridad"

  - type: input
    id: story_points
    attributes:
      label: "Puntos de Historia"
      description: "Estimación en story points para este ticket."
      placeholder: "Ejemplo: 5"

  - type: textarea
    id: attachments
    attributes:
      label: "Adjuntos o Evidencia"
      description: "Capturas de pantalla, logs de error, archivos relacionados."
      placeholder: "Sube imágenes o archivos relevantes aquí."
