export interface User {
  id: number
  name: string
  created_at: string
  updated_at: string
}

export interface Publication {
  id: number
  user_id: number
  title: string
  text: string
  created_at: string
  updated_at: string
  source: 'cache' | 'database'
}

export interface PaginatedPublications {
  items: Publication[]
  total: number
  limit: number
  offset: number
}


async function request<T>(
  url: string,
  options: RequestInit = {},
): Promise<T> {
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
    ...(options.headers as Record<string, string> || {}),
  }

  const res = await fetch(url, { ...options, headers })

  if (!res.ok) {
    const body = await res.json().catch(() => ({}))
    throw new Error(body.detail || `HTTP ${res.status}`)
  }

  if (res.status === 204) return undefined as T
  return res.json()
}

export async function getPublications(
  userId: number,
  limit = 20,
  offset = 0,
): Promise<PaginatedPublications> {
  return request(`/api/publications/user/${userId}?limit=${limit}&offset=${offset}`)
}

